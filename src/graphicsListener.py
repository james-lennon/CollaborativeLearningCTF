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

        # self.states = [[],[]]
        # self.scores = []

        # self.width  = width
        # self.height = height
        # self.game   = game

        # self.flag_spawn_positions = [
        #         (width/2.0, height/10.),
        #         (width/2.0, height*9./10.)
        #     ]
        # self.flag_positions = copy.copy(self.flag_spawn_positions)
        # print "FLAG POSITIONS"
        # print game_state.flag_positions
        
        
        linex = game_state.height * self.scale * 0.5
        self.w.create_line(0, linex, game_state.width*self.scale, linex)
        for j in (0,1):
            for i in xrange(len(game_state.states[j])):
                radius = config.PLAYER_RADIUS * self.scale

                flag_x = game_state.flag_positions[j][0]*self.scale
                flag_y = game_state.flag_positions[j][1]*self.scale
                # self.w.create_rectangle(flag_x, flag_y, flag_x+radius, flag_y+radius, fill="blue")

                s = game_state.states[j][i]
                x = self.scale*s.pos[0]
                y = self.scale*s.pos[1]
                if j == 1: 
                    self.w.create_oval(x, y, x+radius, y+radius, fill="green")
                    self.w.create_rectangle(flag_x, flag_y, flag_x+radius, flag_y+radius, fill="green")
                elif j == 0:
                    self.w.create_oval(x, y, x+radius, y+radius, fill="red")
                    self.w.create_rectangle(flag_x, flag_y, flag_x+radius, flag_y+radius, fill="red")


        self.master.update_idletasks()
        self.master.update()
