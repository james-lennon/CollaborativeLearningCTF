from game import *
from agent import *
from testAgents import *
from terminalListener import *
import time

class DebugListener(GameListener):

	def handle_loop(self, game_state):
		print "STATE UPDATE"
		print "* team 0: {}".format(map(lambda s: s.pos, game_state.states[0]))
		print "* team 1: {}".format(map(lambda s: s.pos, game_state.states[1]))
		print

game = Game(50, 50)

agent1 = RandomAgent()
agent2 = SimpleLearningAgent()

# add agents
game.add_agent(agent1, (0,0), 0)
game.add_agent(agent2, (0,50), 1)

# add listener
game.add_listener(DebugListener())
game.add_listener(TerminalListener())

# simulate game
iterations = 10000

game.start()

for _ in xrange(iterations):
	game.loop()
	# time.sleep(.05)

agent2.save_weights("weights.txt")