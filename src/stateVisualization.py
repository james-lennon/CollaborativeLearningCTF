from Tkinter import *
from model import Action
from qFunction import QFunction


class StateVisualization:

    def __init__(self):
        pass

def colorString(r,g,b):

    color = '#%02x%02x%02x' % (r, g, b)
    return color

def visualize_state(game_state, state, scale = 5.0, resolution = 20, value_clip=100):

    game = game_state.game

    master = Tk()
    w      = Canvas(master, width=game.width*scale, height=game.height*scale)
    w.pack()

    tile_width  = float(game.width) / resolution * scale
    tile_height = float(game.height) / resolution * scale

    for x in xrange(resolution):
        for y in xrange(resolution):
            state.pos = (x, y)
            value     = QFunction.evaluate(state.q_features(Action.stay))
            scaled_value = (value + value_clip) / float(2*value_clip)
            scaled_value = min(1, max(scaled_value, 0))
            color = colorString(scaled_value*255,0,0)
            w.create_rectangle(x*tile_width, y*tile_height, (x+1)*tile_width, (y+1)*tile_height, fill=color)

    master.mainloop()