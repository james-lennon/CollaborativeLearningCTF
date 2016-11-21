from model import *


class Game(object):

	def __init__(self, width, height, state_resolution):
		self.width            = width
		self.height           = height
		self.state_resolution = state_resolution

		self.transition_model = TransitionModel()
		self.reward_model     = RewardModel()

		self.agents    = [[],[]]
		self.listeners = []
		self.gameState = GameState()

	def add_agent(self, agent, team):

		# check valid team
		if team not in (0,1):
			print "ERROR: Invalid team {}; must be 0 or 1.".format(team)
			return

		self.agents[team].append(agent)

	def add_listener(self, listener):
		self.listeners.append(listener)

	def loop(self):
		# update game state
		

		# notify listeners
		map(lambda l: l.handle_loop(self.gameState), self.listeners)

	def run_agent(self, agent, state):
		action    = agent.choose_action(state)
		new_state = transition_model.apply_action(state, action)
		reward    = reward_model.get_reward(state, action, new_state)

		agent.observe_transition(state, action, reward, new_state)

		return new_state


class GameListener(object):

	def handle_loop(self, gameState):
		pass





