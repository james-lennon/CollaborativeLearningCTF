from agent import Agent
from model import Action
import random
import json

class MoveRightAgent(Agent):

	def choose_action(self, state, game_state):
		return Action.right

	def observe_transition(self, state, action, reward, new_state):
		print reward

class RandomAgent(Agent):

	def choose_action(self, state, game_state):
		return random.choice([Action.stay, Action.up, Action.right, Action.left, Action.down])

	def observe_transition(self, state, action, reward, new_state):
		# print reward
		pass

class SimpleLearningAgent(Agent):

	def __init__(self, alpha = .5, epsilon = .1):
		Agent.__init__(self)

		self.weights = None
		self.alpha   = alpha
		self.epsilon = .3
		self.gamma   = .8

	def init_weights(self, n):
		self.weights = [0 for _ in xrange(n)]

	def value_of_state(self, state_vector):
		return sum(map(lambda i: state_vector[i]*self.weights[i], xrange(len(state_vector))))

	def choose_action(self, state, game_state):

		# check if we haven't initiazed weights yet
		if not self.weights:
			self.init_weights(len(state.q_features(Action.stay)))

		adj = game_state.get_adjacent(state)

		best_action = None
		best_score  = None

		for a in adj:
			score = self.value_of_state(adj[a].q_features(a))
			if best_score is None or score > best_score:
				best_score = score
				best_action = a

		if random.random() < self.epsilon:
			return random.choice(Action.all_actions())

		# self.epsilon *= .95
		return best_action

	def observe_transition(self, state, action, reward, new_state):

		state_vector     = state.q_features(action)

		best_new_score   = max(map(lambda a: self.value_of_state(new_state.q_features(a)), 
								Action.all_actions()))

		delta = self.gamma * best_new_score + reward - self.value_of_state(state_vector)

		update = lambda (w, f): w + self.alpha*delta*f

		self.weights = map(update, zip(self.weights, state_vector))

		# print "pos: {}, action: {}, reward: {}".format(state.pos, action, reward)
		# print "score: {}, new score: {}".format(self.value_of_state(state_vector), best_new_score)
		# print "delta: {}".format(delta)
		# print "flag distance feature: {}".format(state_vector[2])
		# print "flag distance feature weight: {}".format(self.weights[2])
		# print "player distance feature weight: {}".format(self.weights[0])

		self.alpha *= .999
		# self.epsilon *= .999

	def save_weights(self, filename):

		with open(filename, "w") as writefile:
			writefile.write(json.dumps(self.weights))






