from game import *
from agent import *
from testAgents import *
from heuristicAgent import *
from neuralAgent import *
from terminalListener import *
import time
import atexit
import sys
from graphicsListener import GraphicsListener
from teamAgents import *
from stateVisualization import *

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
	game  = Game(100, 100)
	agent = QLearningAgent(alpha=.2, alpha_decay=1.0, epsilon=.5)

	if load:
		agent.load_weights("single_agent_weights.txt")
		agent.alpha = 0
		agent.epsilon = .01

	# add agents
	game.add_agent(agent, (25,15), 0)

	# simulate game
	iterations = 50000

	atexit.register(lambda: agent.save_weights("single_agent_weights.txt"))

	game.start()

	# agent.debug = True
	if not load: run_for_iterations(game, 10000)

	game.add_listener(GraphicsListener(game))

	for _ in xrange(iterations):
		game.loop()
		time.sleep(.05)

def obstacle_test(load = False):
	game = Game(100, 100)

	agent1 = Agent()
	agent1b = Agent()
	agent1c = Agent()
	agent1d = Agent()
	agent2 = QLearningAgent(epsilon=0.5, alpha=.2, alpha_decay = 1.0)

	if load:
		agent2.load_weights("obstacle_weights.txt")
		agent2.alpha = 0

	# add agents
	game.add_agent(agent1, (53,15), 0)
	game.add_agent(agent1b, (47,20), 0)
	game.add_agent(agent1c, (53,30), 0)
	game.add_agent(agent1d, (47,40), 0)
	game.add_agent(agent2, (0,0), 1)

	# simulate game
	iterations = 10000

	atexit.register(lambda: agent2.save_weights("obstacle_weights.txt"))

	game.start()
	# agent2.debug = True
	if not load: run_for_iterations(game, iterations)

	agent2.debug = True
	game.add_listener(GraphicsListener(game))
	agent2.epsilon = 0.1

	for _ in xrange(iterations):
		game.loop()
		time.sleep(.05)

def team_test(load=False):
	game = Game(100, 100)

	agent1 = Agent()
	agent1b = Agent()
	agent2 = QLearningAgent(epsilon=0.5, alpha=.2, alpha_decay=1.0)
	agent2b = QLearningAgent(epsilon=0.5, alpha=.2, alpha_decay=1.0)

	if load:
		agent2.load_weights("team_weights.txt")
		agent2.alpha = 0

	# add agents
	game.add_agent(agent1, (47,30), 0)
	game.add_agent(agent1b, (53,30), 0)
	game.add_agent(agent2, (0,0), 1)
	game.add_agent(agent2b, (0,50), 1)

	# simulate game
	iterations = 10000

	atexit.register(lambda: agent2.save_weights("team_weights.txt"))

	game.start()
	# agent2.debug = True
	# if not load: run_for_iterations(game, iterations)

	agent2.debug = True
	game.add_listener(TerminalListener())
	game.add_listener(GraphicsListener(game))

	agent2.epsilon = 0
	agent2b.epsilon = 0
	game.add_listener(GraphicsListener(game))
	agent2.epsilon = 0.01
	agent2b.epsilon = 0.01
	
	game.add_listener(GraphicsListener(game))
	agent2.epsilon = 0.01
	agent2b.epsilon = 0.01

	for _ in xrange(iterations):
		game.loop()
		time.sleep(.05)

def enemy_test(load=False):
	game = Game(100, 100)

	agent1 = HeuristicAgent()
	agent1b = HeuristicAgent()
	agent1c = HeuristicAgent()
	agent1d = HeuristicAgent()
	agent2 = QLearningAgent(epsilon=0.2, alpha=.2, alpha_decay=1.0)
	agent2b = QLearningAgent(epsilon=0.5, alpha=.2, alpha_decay=1.0)
	agent2c = QLearningAgent(epsilon=0.5, alpha=.2, alpha_decay=1.0)
	agent2d = QLearningAgent(epsilon=0.5, alpha=.2, alpha_decay=1.0)

	if load:
		QFunction.load("enemy_weights.txt")
		game.set_team_agent(CollaborativeTeamAgent(), 1)
		agent2.alpha = 0
		agent2b.alpha = 0

	# add agents
	game.add_agent(agent1, (5,10), 0)
	game.add_agent(agent1b, (95,10), 0)

	game.add_agent(agent2, (100,50), 1)
	game.add_agent(agent2b, (0,50), 1)

	# simulate game
	iterations = 10000

	if not load: atexit.register(lambda: QFunction.save("enemy_weights.txt"))

	game.start()
	# agent2.debug = True
	if not load:
		run_for_iterations(game, iterations)

	agent2.debug = True
	game.add_listener(GraphicsListener(game))

	for _ in xrange(iterations):
		game.loop()
		time.sleep(.05)

def learning_enemies_test(load=False):
	game = Game(100, 100)

	agent1 = QLearningAgent(epsilon=0.2, alpha=.2, alpha_decay=1.0)
	agent1b = HeuristicAgent()

	agent2 = QLearningAgent(epsilon=0.2, alpha=.2, alpha_decay=1.0)
	agent2b = HeuristicAgent()

	if load:
		QFunction.load("learning_weights.txt")
		game.set_team_agent(CollaborativeTeamAgent(), 1)
		agent2.alpha = 0
		agent2b.alpha = 0

	# add agents
	game.add_agent(agent1, (5,10), 0)
	game.add_agent(agent1b, (95,10), 0)

	game.add_agent(agent2, (100,50), 1)
	game.add_agent(agent2b, (100,50), 1)

	# simulate game
	iterations = 10000

	if not load: atexit.register(lambda: QFunction.save("learning_weights.txt"))

	game.start()
	# agent2.debug = True
	if not load:
		run_for_iterations(game, iterations)

	agent2.debug = False
	game.add_listener(GraphicsListener(game))

	for _ in xrange(iterations):
		game.loop()
		time.sleep(.05)

def visualize_test():

	game = Game(100, 100)

	agent1 = QLearningAgent(epsilon=0.2, alpha=.2, alpha_decay=1.0)
	agent1b = HeuristicAgent()

	agent2 = QLearningAgent(epsilon=0.2, alpha=.2, alpha_decay=1.0)
	agent2b = HeuristicAgent()

	QFunction.load("learning_weights.txt")
	game.set_team_agent(CollaborativeTeamAgent(), 1)
	agent2.alpha = 0
	agent2b.alpha = 0

	# add agents
	game.add_agent(agent1, (5,10), 0)
	game.add_agent(agent1b, (95,10), 0)

	game.add_agent(agent2, (100,50), 1)
	game.add_agent(agent2b, (100,50), 1)

	# simulate game
	iterations = 10000

	game.start()

	graphics = GraphicsListener(game, clear_screen=False)
	game.add_listener(StateVisualization(game, 1, 0, root=graphics.master, canvas=graphics.w))
	game.add_listener(graphics)

	for _ in xrange(iterations):
		game.loop()
		time.sleep(.05)


# single_agent_test(True)
# obstacle_test()
# neural_test(True)
# team_test()
enemy_test()
# team_test(True)
# enemy_test(True)
# learning_enemies_test(True)
visualize_test()