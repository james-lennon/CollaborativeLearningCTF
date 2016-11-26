from enum import Enum
import config
import util
import copy
import math
import time

class Action(Enum):
	stay       = (0,0)
	up         = (0,1)
	up_right   = (1,1)
	right      = (1,0)
	down_right = (1,-1)
	down       = (0,-1)
	down_left  = (-1,-1)
	left       = (-1,0)
	up_left    = (-1,1)

	@staticmethod
	def all_actions():
		return [Action.stay, Action.up, Action.up_right, Action.right, 
				Action.down_right, Action.down, Action.down_left, 
				Action.left, Action.up_left]

class State(object):

	def __init__(self, game, num):#, dist_team, dist_opps, have_flag, enemy_side, flag_taken, dist_flag, dist_opp_flag, jail):
		self.team = None # either 0 or 1 for which team the State is on
		self.team_positions = []
		self.opp_positions = []
		self.has_flag = False
		self.enemy_side = False
		self.flag_taken = False
		self.dist_flag = 0
		self.dist_opp_flag = 0
		self.dist_base = 0
		self.pos = (0,0)
		self.jail = False
		self.tagging = False

		self.game = game
		self.num  = num

	def list_representation(self):

		max_dist  = math.sqrt(self.game.width**2 + self.game.height**2)
		normalize = lambda d: d / max_dist

		return    map(normalize, self.dist_team)  \
		        + map(normalize, self.dist_opps)  \
		        + [normalize(self.dist_flag)]     \
				+ [normalize(self.dist_opp_flag)] \
				+ [int(self.has_flag)]            \
				+ [int(self.flag_taken)]          \
				+ [int(self.enemy_side)]

	def q_features(self, action):
		new_pos   = util.normalized_move(self.pos, action, config.PLAYER_SPEED)
		new_pos   = util.make_in_range(new_pos, self.game.width, self.game.height)
		pos_delta = lambda p: util.distance(new_pos, p) - util.distance(self.pos, p)

		other_team = self.team ^ 1

		team_pos = []
		for s in self.game.game_state.states[self.team]:
			if s.num != self.num:
				team_pos.append(s.pos)

		base_pos     = self.game.game_state.flag_spawn_positions[self.team]
		opp_flag_pos = self.game.game_state.flag_positions[other_team]

		if self.has_flag:
			opp_flag_delta = 0
			target_delta   = pos_delta(base_pos)
		else:
			opp_flag_delta = pos_delta(opp_flag_pos)
			target_delta   = 0

		if not self.has_flag:
			take_flag    = util.distance(new_pos, opp_flag_pos) <= config.PLAYER_RADIUS
			capture_flag = False
		else:
			take_flag    = False
			capture_flag = util.distance(new_pos, base_pos) <= config.PLAYER_RADIUS

		if take_flag:
			opp_flag_delta = 0
		if capture_flag:
			target_delta = 0

		if self.jail:
			opp_flag_delta = 0
			target_delta   = 0

		return [opp_flag_delta] \
			 + [target_delta] \
			 + [int(take_flag)] \
			 + [int(capture_flag)] \
			 + [int(self.jail)] \
			 + [int(self.tagging)] \
			 + [1.0] # bias
			 # \
			 # map(pos_delta, team_pos) \
			 # + map(pos_delta, map(lambda x: x.pos, self.game.game_state.states[other_team])) \
			 # +
			 # + [int(self.enemy_side)]
			 # + [pos_delta(self.game.game_state.flag_positions[self.team])] \


class GameState(object):
	def __init__(self, width, height, game):
		self.states = [[],[]]
		self.scores = []

		self.width  = width
		self.height = height
		self.game   = game

		self.flag_spawn_positions = [
				(width/2.0, height/10.),
				(width/2.0, height*9./10.)
			]
		self.flag_positions = copy.copy(self.flag_spawn_positions)

	def get_adjacent(self, state):

		# dictionary of action -> state
		result = {}

		for a in Action.all_actions():
			result[a] = self.game.transition_model.apply_action(state, a, self)

		return result


class TransitionModel(object):
	
	def __init__(self):
		self.jail_pos = (-1,-1)

	def handle_tagging(self, state):

		# return if we're touching an enemy
		touching = any(map(lambda x: 
			util.distance(state.pos, x) <= config.PLAYER_RADIUS, state.opp_positions))

		if not touching: return

		state.tagging = False
		if state.enemy_side or state.has_flag:
			state.jail     = True
			state.pos      = self.jail_pos
			state.has_flag = False
		elif not state.enemy_side:
			state.tagging = True


	def is_in_jail(self, state):
		return state.pos == self.jail_pos

	def apply_action(self, old_state, action, game_state):

		# make duplicate so we don't modify state
		state = copy.copy(old_state)

		# if in jail, move out of jail (for now)
		if state.jail:
			state.jail = False
			# TODO: make spawn point
			state.pos  = (0,0)

		# only activate tagging flag for one turn
		if state.tagging:
			state.tagging = False

		# move to new position if not in jail
		if not state.jail:
			new_pos   = util.normalized_move(state.pos, action, config.PLAYER_SPEED)
			state.pos = util.make_in_range(new_pos, game_state.width, game_state.height)

		# update enemy side
		halfway = game_state.height / 2
		if state.pos[1] > halfway and state.team == 0:
			state.enemy_side = True
		else:
			state.enemy_side = False

		# get team and opponent distances
		other_team     = state.team ^ 1 # use XOR operator to toggle team

		team_pos = []
		for s in game_state.states[state.team]:
			if s.num != state.num:
				team_pos.append(s.pos)

		state.team_positions = team_pos
		state.opp_positions  = map(lambda x: x.pos, game_state.states[other_team])

		state.dist_flag     = util.distance(state.pos, game_state.flag_positions[state.team])
		state.dist_opp_flag = util.distance(state.pos, game_state.flag_positions[other_team])
		state.dist_base     = util.distance(state.pos, game_state.flag_spawn_positions[state.team])

		# if state.has_flag:
		# 	opp_flag_pos = game_state.flag_spawn_positions[state.team]
		# else:
		# 	opp_flag_pos = game_state.flag_positions[other_team]
		# state.dist_opp_flag = util.distance(state.pos, opp_flag_pos)

		if not state.has_flag and state.dist_opp_flag <= config.PLAYER_RADIUS:
			state.has_flag = True

		if state.has_flag and state.dist_base <= config.PLAYER_RADIUS:
			state.has_flag = False

		self.handle_tagging(state)

		return state

	def move_state(self, state, new_pos):
		pass
		

class RewardModel(object):
	
	def __init__(self):
		pass

	def get_reward(self, state, action, new_state, game_state):
		
		# punish for jail
		if new_state.jail and not state.jail:
			return config.JAIL_REWARD

		# reward for tagging
		if new_state.tagging:
			return config.TAGGING_REWARD

		reward = 0

		# reward for taking flag
		if new_state.has_flag and not state.has_flag:
			reward += config.TAKE_FLAG_REWARD
			return reward
		elif state.has_flag and not new_state.has_flag and not state.jail:
			reward += config.CAPTURE_FLAG_REWARD
			return reward

		if state.has_flag:
			opp_flag_delta = 0
			target_delta   = state.dist_base - new_state.dist_base
		else:
			opp_flag_delta = state.dist_opp_flag - new_state.dist_opp_flag
			target_delta   = 0

		# print "OD: {}, TD: {}".format(opp_flag_delta, target_delta)

		q_features = state.q_features(action)

		# reward for moving closer to flag
		reward += config.FLAG_REWARD_WEIGHT * \
					(opp_flag_delta + target_delta)

		return reward
		





