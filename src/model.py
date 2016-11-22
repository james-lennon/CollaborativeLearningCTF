from enum import Enum
import config
import copy

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

class State(object):

	def __init__(self):#, dist_team, dist_opps, have_flag, enemy_side, flag_taken, dist_flag, dist_opp_flag, jail):
		self.team = None # either 0 or 1 for which team the State is on
		self.dist_team = []
		self.dist_opps = []
		self.has_flag = False
		self.enemy_side = False
		self.flag_taken = False
		self.dist_flag = (0,0) 
		self.dist_opp_flag = (0,0)
		self.pos = (0,0)
		self.jail = False


class GameState(object):
	def __init__(self):
		self.states = [[],[]]
		self.game_score = 0


class TransitionModel(object):
	
	def __init__(self):
		self.jail_pos = (-1,-1)

	def is_tagged(self, state):
		
		# check if you can be tagged
		if not state.enemy_side and not state.has_flag:
			return False

		# return if we're touching an enemy
		return any(map(lambda x: x <= config.PLAYER_RADIUS, state.dist_opps))

	def is_in_jail(self, state):
		return state.pos == self.jail_pos

	def apply_action(self, old_state, action, game_state):

		state = copy.copy(old_state)

		if state.jail:
			state.jail = False
			# TODO: make spawn point
			state.pos  = (0,0)

		if self.is_tagged(state): 
			state.jail = True
			state.pos  = jail_pos

		if not state.jail:
			state.pos[0] = state.pos[0] + action.value[0]
			state.pos[1] = state.pos[1] + action.value[1]

		other_team = state.team ^ 1 # use XOR operator to toggle team
		distances  = map(lambda x: , game_state.states[other_team])

		for dist in state.dist_team:
			team_pos[0] = original_pos[0]+dist[0]
			team_pos[1] = original_pos[1]+dist[1]
			dist[0] = team_pos[0] - state.pos[0] 
			dist[1] = team_pos[1] - state.pos[1]


		return state

	def move_state(self, state, new_pos):
		pass
		

class RewardModel(object):
	
	def __init__(self):
		pass

	def get_reward(self, state, action, new_state):
		
		# punish for jail
		if new_state.jail and not state.jail:
			return config.JAIL_REWARD

		# calculate reward for getting closer to flag
		flag_reward = config.FLAG_REWARD_WEIGHT * \
					(new_state.dist_opp_flag - state.dist_opp_flag)

		return flag_reward
		





