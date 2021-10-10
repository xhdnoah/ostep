# from this sort of thing
# a forks b
# a forks c
# a forks d
# b forks e
# b forks f
# d forks g

# to a process tree
# a --- b --- e
#   |     |
#   |     |- f
#   |- c
#   |
#   |- d --- g

from __future__ import print_function
import random
import string
from optparse import OptionParser


def random_randint(low, high):
    return int(low + random.random() * (high - low + 1))


def random_choice(L):
    return L[random_randint(0, len(L) - 1)]


class Forker:
    def __init__(
        self,
        fork_percentage,
        actions,
        action_list,
        show_tree,
        just_final,
        leaf_only,
        local_reparent,
        print_style,
        solve,
    ):
        self.fork_percentage = fork_percentage
        self.max_actions = actions
        self.action_list = action_list
        self.show_tree = show_tree
        self.just_final = just_final
        self.leaf_only = leaf_only
        self.local_reparent = local_reparent
        self.print_style = print_style
        self.solve = solve

        self.root_name = 'a'

				self.process_list = [self.root_name]
