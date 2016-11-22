from agent import Agent
from model import Action
import random

class MoveRightAgent(Agent):

	def choose_action(self, state, game_state):
		return Action.right

	def observe_transition(self, state, action, reward, new_state):
		print reward

class RandomAgent(Agent):

	def choose_action(self, state, game_state):
		return random.choice([Action.stay, Action.up, Action.right, Action.left, Action.down])

	def observe_transition(self, state, action, reward, new_state):
		print reward

class SimpleLearningAgent(Agent):

	def __init__(self):
		Agent.__init__(self)

		self.weights = None

	def choose_action(self, state, game_state):

		adj = game_state.get_adjacent(state)

		best_action = None
		best_score  = None

		print state.list_representation()

		return Action.stay

	def observe_transition(self, state, action, reward, new_state):
		print reward