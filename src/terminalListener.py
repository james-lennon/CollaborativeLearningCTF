# import Tk class (to create root window)
# Frame class (container for other widgets)
from PIL import Image, ImageTk
from Tkinter import Tk, Label, BOTH
from ttk import Frame, Style

from game import *
import util

class TerminalListener(GameListener):

    def handle_loop(self, game_state):
        # print "\n\n\n\n\n\n\n\n"

        # root = Tk()
        # # specify size of screen, location on screen
        # root.geometry("250x150+300+300")
        # # create instance of application class, feeding in root (Frame object)
        # app = TKRepresent(root, game_state)
        # # enter mainloop 
        # root.mainloop()


        #         self.states = [[],[]]
        # self.scores = []

        # self.width  = width
        # self.height = height
        # self.game   = game

        # self.flag_spawn_positions = [
        #         (width/2.0, height/10.),
        #         (width/2.0, height*9./10.)
        #     ]
        # self.flag_positions = copy.copy(self.flag_spawn_positions)

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



# inherits from Frame container widget
class TKRepresent(Frame):
  
    def __init__(self, parent, game_state):
        # call Frame constructor method
        Frame.__init__(self, parent)   
         
        # save reference to parent widget (TK root window) 
        self.parent = parent
        
        # create user interface 
        self.initUI(game_state)
        
    # method to create user interface
    def initUI(self, game_state):
        # label window title
        # self.parent.title("Simple")
        # pack() is geometry manager
        self.pack(fill=BOTH, expand=1)

        Style().configure("TFrame")
        

        objects = []
        for i in range(len(game_state.states)): 
            for j in range(len(game_state.states[i])):
                if i == 0:
                    team1 = Image.open("team1.png")
                    team1image = ImageTk.PhotoImage(team1)
                    label1 = Label(self, image=team1image)
                    label1.image = team1image
                    label1.place(x=game_state.states[i][j][0], y=game_state.states[i][j][1])
                elif i == 1: 
                    team2 = Image.open("team2.png")
                    team2image = ImageTk.PhotoImage(team2)
                    label2 = Label(self, image=team2image)
                    label2.image = team2image
                    label2.place(x=game_state.states[i][j][0], y=game_state.states[i][j][1])

