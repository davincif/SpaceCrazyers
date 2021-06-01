# third party
import pygame

# internals
from .props import AlignProp, JustifyProp, GrowthDirectionProp
from src.colors import Colors
from src.basic_forms.square import Square


class Container(Square):
    parent = None
    aling = AlignProp.UP_LEFT
    justify = JustifyProp.START
    gorth_direction = GrowthDirectionProp.HORIZONTAL
    show_background = None
    children = []

    def __init__(
        self,
        pos,
        dimension,
        color=Colors.WHITE.value,
        parent=None,
        aling=None,
        justify=None,
        gorth_direction=None,
        show_background=False,
    ):
        Square.__init__(self, pos=pos, dimension=dimension, color=color)

        self.parent = parent
        self.set_aling(aling)
        self.set_justify(justify)
        self.show_background = show_background

    # getts and setters
    def set_aling(self, value: AlignProp):
        if isinstance(value, AlignProp):
            self.aling = value

    def set_justify(self, value: JustifyProp):
        if isinstance(value, JustifyProp):
            self.justify = value

    def set_gorth_direction(self, value: gorth_direction):
        if isinstance(value, gorth_direction):
            self.gorth_direction = value

    # inherited
    def how_to_draw_me(self, screen):
        if(self.show_background):
            super().how_to_draw_me(screen)
        for child in self.children:
            child.how_to_draw_me(screen)

    # public methods
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
