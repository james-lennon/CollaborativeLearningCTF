from game import *
import util

class TerminalListener(GameListener):

	def handle_loop(self, game_state):
		print "\n\n\n\n\n\n\n\n"

		for y in xrange(game_state.height):
			for x in xrange(game_state.width):

				has_agent = False
				for s in game_state.states[0]:
					if util.distance(s.pos, (x,y)) <= 1:
						print "1",
						has_agent = True
				for s in game_state.states[1]:
					if util.distance(s.pos, (x,y)) <= 1:
						print "2",
						has_agent = True
				if not has_agent: print ".",
			print