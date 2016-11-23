from game import *
import util

class TerminalListener(GameListener):

	def handle_loop(self, game_state):
		print "\n\n"

		for x in xrange(game_state.width):
			for y in xrange(game_state.height):

				for s in game_state.states[0]:
					if util.distance(s.pos, (x,y)) < 2:
						print "1",
						continue
				for s in game_state.states[1]:
					if util.distance(s.pos, (x,y)) < 2:
						print "2",
						continue
				print ".",
			print