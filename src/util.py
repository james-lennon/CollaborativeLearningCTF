def EuclidDist(pos1, pos2):
	# print pos1-pos2
	return ((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)**0.5


print EuclidDist((0,0),(1,1))