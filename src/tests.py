from game import *
from agent import *
from testAgents import *
from heuristicAgent import *
from teamAgents import *
from graphicsListener import *

def battle1():
    game = Game(100, 100)

    agent1 = QLearningAgent(epsilon=0.01, alpha=0, alpha_decay=1.0)
    agent1b = QLearningAgent(epsilon=0.01, alpha=0, alpha_decay=1.0)
    agent1c = HeuristicAgent()
    agent1d = HeuristicAgent()
    agent2 = QLearningAgent(epsilon=0.01, alpha=0, alpha_decay=1.0)
    agent2b = QLearningAgent(epsilon=0.01, alpha=0, alpha_decay=1.0)
    agent2c = QLearningAgent(epsilon=0.01, alpha=0, alpha_decay=1.0)
    agent2d = QLearningAgent(epsilon=0.01, alpha=0, alpha_decay=1.0)

    QFunction.load("learning_weights.txt")
    # game.set_team_agent(CollaborativeTeamAgent(), 1)
    agent2.alpha = 0
    agent2b.alpha = 0

    # add agents
    game.add_agent(agent1, (0, 0), 0)
    game.add_agent(agent1b, (100, 0), 0)
    # game.add_agent(agent1c, (95,10), 0)
	# game.add_agent(agent1d, (95,10), 0)
    game.add_agent(agent2, (100,50), 1)
    game.add_agent(agent2b, (0,50), 1)
    # game.add_agent(agent2c, (100,50), 1)
    # game.add_agent(agent2d, (100,50), 1)

	# simulate game
    iterations = 10000

    game.start()
    # game.add_listener(GraphicsListener(game))

    # agent2.debug = True

    for _ in xrange(iterations):
        game.loop()
        # time.sleep(.05)

    print game.game_state.scores

def battle2():
    game = Game(100, 100)

    agent1 = QLearningAgent(epsilon=0.01, alpha=0, alpha_decay=1.0)
    agent1b = QLearningAgent(epsilon=0.01, alpha=0, alpha_decay=1.0)
    agent1c = HeuristicAgent()
    agent1d = HeuristicAgent()
    agent2 = QLearningAgent(epsilon=0.01, alpha=0, alpha_decay=1.0)
    agent2b = QLearningAgent(epsilon=0.01, alpha=0, alpha_decay=1.0)
    agent2c = QLearningAgent(epsilon=0.01, alpha=0, alpha_decay=1.0)
    agent2d = QLearningAgent(epsilon=0.01, alpha=0, alpha_decay=1.0)

    QFunction.load("learning_weights.txt")
    # game.set_team_agent(CollaborativeTeamAgent(), 0)
    # game.set_team_agent(CollaborativeTeamAgent(), 1)
    agent2.alpha = 0
    agent2b.alpha = 0

    # add agents
    game.add_agent(agent1, (0, 0), 0)
    game.add_agent(agent1b, (100, 0), 0)
    # game.add_agent(agent1c, (95,10), 0)
	# game.add_agent(agent1d, (95,10), 0)
    game.add_agent(agent2, (100,50), 1)
    game.add_agent(agent2b, (0,50), 1)
    # game.add_agent(agent2c, (100,50), 1)
    # game.add_agent(agent2d, (100,50), 1)

	# simulate game
    iterations = 10000

    game.start()
    # game.add_listener(GraphicsListener(game))

    # agent2.debug = True

    for _ in xrange(iterations):
        game.loop()
        # time.sleep(.05)

    print game.game_state.scores



battle2()