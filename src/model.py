from enum import Enum
import reward

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
		flag_reward = config.FLAG_REWARD_WEIGHT * 
					(new_state.dist_opp_flag - state.dist_opp_flag)

		return flag_reward
		





