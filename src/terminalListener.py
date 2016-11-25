from game import *
import util

class TerminalListener(GameListener):

	def handle_loop(self, game_state):
		# print "\n\n\n\n\n\n\n\n"

		for y in xrange(game_state.height):
			for x in xrange(game_state.width):

				has_agent = False
				for s in game_state.states[0]:
					if util.distance(s.pos, (x,y)) <= 1:
						char = "B" if s.has_flag else "1"
						print char,
						has_agent = True
				for s in game_state.states[1]:
					if util.distance(s.pos, (x,y)) <= 1:
						char = "A" if s.has_flag else "2"
						print char,
						has_agent = True
				if util.distance(game_state.flag_positions[0], (x,y)) <= 1:
					print "A",
					has_agent = True
				if util.distance(game_state.flag_positions[1], (x,y)) <= 1:
					print "B",
					has_agent = True
				if not has_agent: print ".",
			print