from model import *


class Game(object):

	def __init__(self, width=100, height=100, state_resolution=100):
		self.width            = width
		self.height           = height
		self.state_resolution = state_resolution

		self.transition_model = TransitionModel()
		self.reward_model     = RewardModel()

		self.agents    = [[],[]]
		self.listeners = []
		self.game_state = GameState()

	def add_agent(self, agent, team):

		# check valid team
		if team not in (0,1):
			print "ERROR: Invalid team {}; must be 0 or 1.".format(team)
			return

		self.agents[team].append(agent)

	def add_listener(self, listener):
		self.listeners.append(listener)

	def run_team(self, team):
		self.game_state.states[team] = \
			map(lambda a: 
				self.run_agent(self.agents[team][a], self.game_state.states[team][a]),
				xrange(len(self.agents[team])))

	def loop(self):
		# update game state
		self.run_team(0)
		self.run_team(1)

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





