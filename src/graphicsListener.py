from game import *
from Tkinter import *
import config

class GraphicsListener(GameListener):

    def __init__(self, game):
        self.scale = 5.0

        self.master = Tk()
        self.game   = game
        self.w      = Canvas(self.master, width=game.width*self.scale, height=game.height*self.scale)
        self.w.pack()


    def handle_loop(self, game_state):

        self.w.delete(ALL)

        for j in (0,1):

            for i in xrange(len(game_state.states[j])):
                s = game_state.states[j][i]

                radius = config.PLAYER_RADIUS * self.scale
                x = self.scale*s.pos[0]
                y = self.scale*s.pos[1]

                self.w.create_rectangle(x, y, x+2*radius, y+2*radius)

        self.master.update_idletasks()
        self.master.update()
