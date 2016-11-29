from game import *
from Tkinter import *
import config


# I just made some squares to follow the players, 
# it would be great if you could make them colored circles
# and also show the flag when you get the chance!

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

                if j == 1: 
                    self.w.create_oval(x, y, x+2*radius, y+2*radius, fill="green")
                elif j == 0:
                    self.w.create_oval(x, y, x+2*radius, y+2*radius, fill="red")


        self.master.update_idletasks()
        self.master.update()
