from game import *
from agent import *

class DebugListener(GameListener):

	def handle_loop(self, game_state):
		print "STATE UPDATE"
		print "* team 0: {}".format(map(lambda s: s.pos, game_state.states[0]))
		print "* team 1: {}".format(map(lambda s: s.pos, game_state.states[1]))
		print

class MoveRightAgent(Agent):

	def get_action(self, state):
		return Action.right

game = Game()

agent1 = Agent()
agent2 = MoveRightAgent()

# add agents
game.add_agent(agent1, (0,0), 0)
game.add_agent(agent2, (0,100), 1)

# add listener
game.add_listener(DebugListener())

# simulate game
iterations = 100
for _ in xrange(iterations):
	game.loop()

