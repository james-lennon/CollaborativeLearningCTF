from agent import *
from model import *


class HeuristicAgent(Agent):

    def choose_action(self, state, game_state):
        other_team = state.team ^ 1
        enemy_pos  = map(lambda s: s.pos, game_state.states[other_team])

        adj = game_state.get_adjacent(state)

        min_dist = lambda p: min(map(lambda o: util.distance(p, o), enemy_pos))

        best_action = None
        best_score = None
        for a in adj:
            score = min_dist(adj[a].pos)
            if best_score is None or score < best_score:
                best_action = a
                best_score = score

        threshold = 3 * config.PLAYER_RADIUS

        if best_score <= threshold:
            return best_action

        target = game_state.flag_positions[state.team] if state.has_flag else game_state.flag_positions[other_team]
        best_action = None
        best_score = None
        for a in adj:
            score = util.distance(target, adj[a].pos)
            if best_score is None or score < best_score:
                best_action = a
                best_score = score

        return best_action

    def observe_transition(self, state, action, reward, new_state):
        pass
