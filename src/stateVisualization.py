from Tkinter import *
from copy import copy
from game import GameListener
from model import Action
from qFunction import QFunction


class StateVisualization(GameListener):

    def __init__(self, game, team, num):
        self.scale = 5.0
        self.resolution = 20
        self.value_clip = 30
        self.team = team
        self.num = num

        self.master = Tk()
        self.w      = Canvas(self.master, width=game.width*self.scale, height=game.height*self.scale)
        self.w.pack()

    def handle_loop(self, game_state):

        game = game_state.game
        state = copy(game_state.states[self.team][self.num])

        tile_width  = float(game.width) / self.resolution * self.scale
        tile_height = float(game.height) / self.resolution * self.scale

        for x in xrange(self.resolution):
            for y in xrange(self.resolution):
                state.pos = (x, y)
                value     = QFunction.evaluate(state.q_features(Action.stay))
                # print value
                scaled_value = (value + self.value_clip) / float(2*self.value_clip)
                scaled_value = min(1, max(scaled_value, 0))
                color = colorString(scaled_value*255,0,0)
                self.w.create_rectangle(x*tile_width, y*tile_height, (x+1)*tile_width, (y+1)*tile_height, fill=color)

        self.master.update_idletasks()
        self.master.update()


def colorString(r,g,b):

    color = '#%02x%02x%02x' % (r, g, b)
    return color

# def visualize_state(game_state, state, scale = 5.0, resolution = 20, value_clip=30):
#
#
#
#     tile_width  = float(game.width) / resolution * scale
#     tile_height = float(game.height) / resolution * scale
#
#     for x in xrange(resolution):
#         for y in xrange(resolution):
#             state.pos = (x, y)
#             value     = QFunction.evaluate(state.q_features(Action.stay))
#             # print value
#             scaled_value = (value + value_clip) / float(2*value_clip)
#             scaled_value = min(1, max(scaled_value, 0))
#             color = colorString(scaled_value*255,0,0)
#             w.create_rectangle(x*tile_width, y*tile_height, (x+1)*tile_width, (y+1)*tile_height, fill=color)
#
#     master.update_idletasks()
#     master.update()