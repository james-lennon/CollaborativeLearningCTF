import math

def distance(a, b):
	return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def normalized_move(a, delta):
	magnitude = math.sqrt(delta[0]**2 + delta[1]**2)

	if magnitude == 0:
		return a

	return (a[0] + delta[0]/magnitude, a[1] + delta[1]/magnitude)