# internals
from src.node import Node


class Container(Node):
    size = (30, 10)

    def __init__(self, pos, size):
        Node.__init__(self, pos=pos)
