from game import *
from agent import *

game = Game()

agent1 = Agent()
agent2 = Agent()

game.add_agent(agent1, State(), 0)
game.add_agent(agent2, State(), 1)

iterations = 100

for _ in xrange(iterations):
	game.loop()

