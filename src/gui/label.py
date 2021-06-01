# third party
import pygame

# internals
from .container import Container
from src.colors import Colors


class Label(Container):
    # private attributes
    _font = None
    _text = ''
    _font_family = 'arial'
    _font_size = 12

    # public attributes
    pass

    def __init__(
        self,
        pos,
        dimension=(0, 0),
        color=Colors.RED.value,
        parent=None,
        show_background=False,
        text='',
        font_family=None,
        font_size=None,
    ):
        Container.__init__(
            self,
            pos=pos,
            dimension=dimension,
            color=color,
            parent=parent,
            show_background=show_background
        )

        if text:
            self.text = text
        if font_family is not None:
            self._font_family = font_family
        if font_size is not None:
            self.font_size = font_size

    # getts and setters
    def _set_font(self):
        self._font = pygame.font.SysFont(
            self._font_family,
            self._font_size,
            True,
            False,
        )

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value: str):
        self._text = value
        self._set_font()

    @property
    def font_family(self):
        return self._font_family

    @font_family.setter
    def font_family(self, value: str):
        self._font_family = value
        self._set_font()

    # inherited

    def how_to_draw_me(self, screen):
        if self.parent is None:
            super().how_to_draw_me(screen)

        text = self._font.render(self._text, True, self.color)
        screen.blit(text, self.pos)
