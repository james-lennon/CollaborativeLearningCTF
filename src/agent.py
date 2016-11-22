from model import Action

class Agent(object):

	def __init__(self):
		pass

	def choose_action(self, state, game_state):
		return Action.stay

	def observe_transition(self, state, action, reward, new_state):
		pass


