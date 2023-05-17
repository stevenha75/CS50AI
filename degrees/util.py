class Node():
    def __init__(self, state, parent, action):
        self.state = state  # actor id
        self.parent = parent  # previous actor id
        self.action = action  # movie id to arrive at current actor 


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            # retrieve the last element
            node = self.frontier[-1]
            # create a list from the start to the last element
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    # overrided remove. Instead of a stack last-in first out; 
    # it becomes first in first out (queue)
    def remove(self):
        if self.empty():
            raise exception("empty frontier")
        else:
            # saves first element
            node = self.frontier[0]
            # creates new array from the second element to the end
            self.frontier = self.frontier[1:]
            return node
