

class Game(object):

	def __init__(self, width, height, state_resolution):
		self.width = width
		self.height = height
		self.state_resolution = state_resolution

		self.listeners = []
		self.gameState = GameState()

	def add_listener(self, listener):
		self.listeners.append(listener)

	def loop(self):
		# TODO: update game state

		# notify listeners
		map(lambda l: l.handle_loop(self.gameState), self.listeners)

	def run_agent(self, agent):
		pass

	def apply_action(self, state, action):
		pass


class GameListener(object):

	def handle_loop(self, gameState):
		pass