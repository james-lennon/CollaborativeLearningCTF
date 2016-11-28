

class QFunction(object):

    weights = None

    @classmethod
    def setup(cls, n):
        cls.weights = [0 for _ in xrange(n)]

    @classmethod
    def evaluate(cls, state_vector):
        return sum(map(lambda i: state_vector[i] * cls.weights[i], xrange(len(state_vector))))

    @classmethod
    def learn(cls, alpha, state_vector, action, old, new):
        delta = new - old
        update = lambda (w, f): w + alpha * delta * f
        cls.weights = map(update, zip(cls.weights, state_vector))

