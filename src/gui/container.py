# third party
import pygame

# internals
from .props import AlignProp, JustifyProp, GrowthDirectionProp
from src.colors import Colors
from src.basic_forms.square import Square


class Container(Square):
    aling = AlignProp.UP_LEFT
    justify = JustifyProp.START
    gorth_direction = GrowthDirectionProp.HORIZONTAL
    show_background = None
    margin = (0, 0, 0, 0)
    children = []

    def __init__(
        self,
        pos,
        dimension,
        parent=None,
        color=Colors.WHITE.value,
        aling=None,
        justify=None,
        gorth_direction=None,
        show_background=False,
        margin=None,
    ):
        Square.__init__(self, pos=pos, dimension=dimension, color=color)
        self.show_background = show_background

        self.set_parent(parent)
        self.set_aling(aling)
        self.set_justify(justify)

        if margin is not None:
            self.margin = margin

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
    def how_to_draw_me(self, screen, draw_children=True, pos_modifier=None):
        if self.show_background:
            modifier = (self.margin[0], self.margin[1])
            if pos_modifier is not None:
                modifier[0] += pos_modifier[0]
                modifier[1] += pos_modifier[1]

            super().how_to_draw_me(screen, modifier)

        if draw_children:
            for child in self.children:
                child.how_to_draw_me(screen)

    # public methods
    def add_child(self, child):
        child.set_parent(self)
        self.children.append(child)
