from game import *
from agent import *
from testAgents import *
from neuralAgent import *
from terminalListener import *
import time
import atexit
import sys

class DebugListener(GameListener):

	def handle_loop(self, game_state):
		print "STATE UPDATE"
		print "* team 0: {}".format(map(lambda s: s.pos, game_state.states[0]))
		print "* team 1: {}".format(map(lambda s: s.pos, game_state.states[1]))
		print

def run_for_iterations(game, iterations):

	for i in xrange(iterations):
		game.loop()
		if i % (iterations/100) == 0:
			sys.stdout.write("\r{:d}%".format(100*i/iterations))
			sys.stdout.flush()

def single_agent_test(load=False):
	game  = Game(50, 30)
	agent = QLearningAgent(epsilon=.5)

	if load:
		agent.load_weights("single_agent_weights.txt")

	# add agents
	game.add_agent(agent, (25,15), 0)

	# simulate game
	iterations = 5000

	atexit.register(lambda: agent.save_weights("single_agent_weights.txt"))

	game.start()

	agent.debug = True
	# run_for_iterations(game, 50000)

	game.add_listener(TerminalListener())

	# agent.alpha = 0
	# agent.epsilon = 0

	for _ in xrange(iterations):
		game.loop()
		time.sleep(.05)

def obstacle_test(load = False):
	game = Game(50, 30)

	agent1 = Agent()
	agent1b = Agent()
	agent2 = QLearningAgent(epsilon=0.5, alpha_decay = 0.999)

	if load:
		agent2.load_weights("obstacle_weights.txt")

	# add agents
	game.add_agent(agent1, (15,10), 0)
	game.add_agent(agent1b, (35,10), 0)
	game.add_agent(agent2, (0,0), 1)

	# simulate game
	iterations = 50000

	atexit.register(lambda: agent2.save_weights("obstacle_weights.txt"))

	game.start()
	# agent2.debug = True
	run_for_iterations(game, iterations)

	agent2.debug = True
	game.add_listener(TerminalListener())
	# agent2.epsilon = 0.2

	for _ in xrange(iterations):
		game.loop()
		time.sleep(.05)

def neural_test(load=False):
	game  = Game(50, 30)
	agent = NeuralAgent()

	if load:
		agent.load_weights("neural_weights.txt")

	# add agents
	game.add_agent(agent, (25,15), 0)

	# simulate game
	iterations = 10000

	atexit.register(lambda: agent.save_weights("neural_weights.txt"))

	game.start()

	# run_for_iterations(game, 50000)

	game.add_listener(TerminalListener())

	# agent.alpha = 0
	# agent.epsilon = 0

	for _ in xrange(iterations):
		game.loop()
		time.sleep(.05)

single_agent_test(True)
# obstacle_test(True)
# load_test()
# neural_test(True)
