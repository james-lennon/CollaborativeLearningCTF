from model import Action

class Agent(object):

	def __init__(self):
		pass

	def choose_action(self, state):
		return Action.STAY

	def observe_transition(self, state, action, reward, new_state):
		pass


