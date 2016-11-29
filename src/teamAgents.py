from agent import *
from qFunction import QFunction

class CollaborativeTeamAgent(TeamAgent):

    def best_combination(self, i, states, game_state):

        if i >= len(states):
            return ([], 0)

        best_score  = None
        best_actions = None
        for a in Action.all_actions():

            actions, next = self.best_combination(i + 1, states, game_state)
            score = QFunction.evaluate(states[i].q_features(a)) + next
            if best_score is None or score > best_score:
                best_score = score
                best_actions = [a] + actions

        return (best_actions, best_score)

    def choose_actions(self, game_state, team):
        return self.best_combination(0, game_state.states[team], game_state)[0]
