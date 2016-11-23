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

game = Game(50, 30)

agent1a = RandomAgent()
agent1b = RandomAgent()
agent2a = QLearningAgent()
agent2b = QLearningAgent()

# add agents
game.add_agent(agent1a, (25,15), 0)
# game.add_agent(agent1b, (25,15), 0)
# game.add_agent(agent2a, (0,0), 1)
game.add_agent(agent2b, (25,0), 1)

# add listener
# game.add_listener(DebugListener())

# simulate game
iterations = 50000

game.start()
game.add_listener(TerminalListener())

for _ in xrange(iterations):
	game.loop()
	time.sleep(.05)

agent2a.epsilon = 0
agent2b.epsilon = 0

for _ in xrange(iterations):
	game.loop()
	time.sleep(.05)

agent2.save_weights("weights.txt")



