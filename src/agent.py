from model import Action

class Agent(object):

	def __init__(self):
		pass

	def choose_action(self, state, game_state):
		return Action.stay

	def observe_transition(self, state, action, reward, new_state):
		pass


class TeamAgent(object):

	def choose_actions(self, game_state, team):
		return [Action.stay for _ in game_state.states[team]]