from enum import Enum
import numpy as np

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

	# def __init__(self, dist_team, dist_opps, have_flag, enemy_side, flag_taken, dist_flag, dist_opp_flag, jail):
	def __init__(self):#, dist_team, dist_opps, have_flag, enemy_side, flag_taken, dist_flag, dist_opp_flag, jail):
		self.global_positions = [[],[]]
		self.team = None # either 0 or 1 for which team the State is on
		self.dist_team = []
		self.dist_opps = []
		self.have_flag = False
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
		pass

	def apply_action(self, state, action):
		original_pos = state.pos
		state.pos[0] = state.pos[0] + action.value[0]
		state.pos[1] = state.pos[1] + action.value[1]
		if state.pos is a jail state: 
			state.jail = True 
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

	def get_reward(self, state, action, state):
		return 0
		





