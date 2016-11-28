from game import *
from agent import *
from testAgents import *
from heuristicAgent import *
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
	agent = QLearningAgent(alpha_decay=.99, epsilon=.5)

	if load:
		agent.load_weights("single_agent_weights.txt")
		agent.alpha = 0

	# add agents
	game.add_agent(agent, (25,15), 0)

	# simulate game
	iterations = 5000

	atexit.register(lambda: agent.save_weights("single_agent_weights.txt"))

	game.start()

	agent.debug = True
	# run_for_iterations(game, 50000)

	game.add_listener(TerminalListener())

	for _ in xrange(iterations):
		game.loop()
		time.sleep(.05)

def obstacle_test(load = False):
	game = Game(50, 30)

	agent1 = Agent()
	agent1b = Agent()
	agent2 = QLearningAgent(epsilon=0.5, alpha_decay = 0.99)

	if load:
		agent2.load_weights("obstacle_weights.txt")
		agent2.alpha = 0

	# add agents
	game.add_agent(agent1, (5,10), 0)
	game.add_agent(agent1b, (27,10), 0)
	game.add_agent(agent2, (0,0), 1)

	# simulate game
	iterations = 50000

	atexit.register(lambda: agent2.save_weights("obstacle_weights.txt"))

	game.start()
	# agent2.debug = True
	run_for_iterations(game, iterations)

	agent2.debug = True
	game.add_listener(TerminalListener())
	agent2.epsilon = 0

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

def team_test(load=False):
	game = Game(50, 30)

	agent1 = Agent()
	agent1b = Agent()
	agent2 = QLearningAgent(epsilon=0.5, alpha_decay = 0.99)
	agent2b = QLearningAgent(epsilon=0.5, alpha_decay = 0.99)

	if load:
		agent2.load_weights("team_weights.txt")
		agent2.alpha = 0

	# add agents
	game.add_agent(agent1, (5,10), 0)
	game.add_agent(agent1b, (25,10), 0)
	game.add_agent(agent2, (0,0), 1)
	game.add_agent(agent2b, (0,50), 1)

	# simulate game
	iterations = 10000

	atexit.register(lambda: agent2.save_weights("team_weights.txt"))

	game.start()
	# agent2.debug = True
	run_for_iterations(game, iterations)

	agent2.debug = True
	game.add_listener(TerminalListener())
	agent2.epsilon = 0
	agent2b.epsilon = 0

	for _ in xrange(iterations):
		game.loop()
		time.sleep(.05)

def enemy_test(load=False):
	game = Game(50, 30)

	agent1 = HeuristicAgent()
	agent2 = QLearningAgent(epsilon=0.5, alpha_decay = 0.99)
	# agent2b = QLearningAgent(epsilon=0.5, alpha_decay = 0.99)

	if load:
		agent2.load_weights("enemy_weights.txt")
		agent2.alpha = 0

	# add agents
	game.add_agent(agent1, (5,10), 0)
	game.add_agent(agent2, (0,0), 1)
	# game.add_agent(agent2b, (0,50), 1)

	# simulate game
	iterations = 10000

	atexit.register(lambda: agent2.save_weights("enemy_weights.txt"))

	game.start()
	# agent2.debug = True
	run_for_iterations(game, iterations)

	agent2.debug = True
	game.add_listener(TerminalListener())
	# agent2.epsilon = 0
	# agent2b.epsilon = 0

	for _ in xrange(iterations):
		game.loop()
		time.sleep(.05)



# single_agent_test(True)
# obstacle_test()
# neural_test(True)
# team_test()
enemy_test()
