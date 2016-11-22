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

	def __init__(self, alpha = .5, epsilon = .1):
		Agent.__init__(self)

		self.weights = None
		self.alpha   = alpha
		self.epsilon = .5

	def init_weights(self, n):
		self.weights = [0 for _ in xrange(n)]

	def value_of_state(self, state_vector):
		return sum(map(lambda i: state_vector[i]*self.weights[i], xrange(len(state_vector))))

	def choose_action(self, state, game_state):

		state_vector = state.list_representation()

		if not self.weights:
			self.init_weights(len(state_vector))

		adj = game_state.get_adjacent(state)

		best_action = None
		best_score  = None

		for a in adj:
			score = self.value_of_state(adj[a].list_representation())
			if best_score is None or score > best_score:
				best_score = score
				best_action = a

		if random.random() < self.epsilon:
			return random.choice(Action.all_actions())

		self.epsilon *= .95
		return best_action

	def observe_transition(self, state, action, reward, new_state):

		state_vector     = state.list_representation()
		new_state_vector = new_state.list_representation()

		delta = self.value_of_state(new_state_vector) + reward - self.value_of_state(state_vector)

		update = lambda (w, f): w + self.alpha*delta*f

		self.weights = map(update, zip(self.weights, state_vector))

		print self.weights
		print state_vector






