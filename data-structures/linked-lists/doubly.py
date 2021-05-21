from .singly import Node

class DNode(Node):

    def __init__(self, value, prev_node=None, next_node=None):
        super().__init__(value, next_node=next_node)
        self.prev_node = prev_node


