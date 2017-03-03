from game import *
from Tkinter import *
import config


# I just made some squares to follow the players, 
# it would be great if you could make them colored circles
# and also show the flag when you get the chance!

class GraphicsListener(GameListener):

    def __init__(self, game, clear_screen=True):
        self.scale = 5.0

        self.master = Tk()
        self.game   = game
        self.w      = Canvas(self.master, width=game.width*self.scale, height=game.height*self.scale)
        self.w.pack()

        self.clear_screen = clear_screen

    def handle_loop(self, game_state):

        if self.clear_screen:
            self.w.delete(ALL)
        
        linex = game_state.height * self.scale * 0.5
        self.w.create_line(0, linex, game_state.width*self.scale, linex)
        radius = config.PLAYER_RADIUS * self.scale


        for j in (0,1):
            flag_x = game_state.flag_positions[j][0]*self.scale
            flag_y = game_state.flag_positions[j][1]*self.scale

            if j == 1:
                self.w.create_rectangle(flag_x, flag_y, flag_x+radius, flag_y+radius, fill="red")
            else:
                self.w.create_rectangle(flag_x, flag_y, flag_x+radius, flag_y+radius, fill="blue")

            for i in xrange(len(game_state.states[j])):
                s = game_state.states[j][i]
                x = self.scale*s.pos[0]
                y = self.scale*s.pos[1]
                if j == 1: 
                    self.w.create_text(game_state.width*self.scale*0.5, game_state.height*self.scale, anchor = S, text = "Score: " + str(game_state.scores[j]))
                    if x == flag_x and y == flag_y:
                        self.w.create_oval(1.05*x, 1.05*y, x+radius, y+radius, fill="red")
                    else: 
                        self.w.create_oval(x, y, x+radius, y+radius, fill="red")
                elif j == 0:
                    self.w.create_text(game_state.width*self.scale*0.5, 0, anchor = N, text = "Score: " + str(game_state.scores[j]))
                    if x == flag_x and y == flag_y:
                        self.w.create_oval(1.05*x, 1.05*y, x+radius, y+radius, fill="blue")
                    else: 
                        self.w.create_oval(x, y, x+radius, y+radius, fill="blue")                    

        self.master.update_idletasks()
        self.master.update()
