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
    _text_rendered = None

    # public attributes
    text_color = Colors.RED.value

    def __init__(
        self,
        pos,
        text_color=None,
        color=Colors.BLUE.value,
        parent=None,
        show_background=False,
        text='',
        font_family=None,
        font_size=None,
    ):
        Container.__init__(
            self,
            pos=pos,
            dimension=(0, 0),
            color=color,
            parent=parent,
            show_background=show_background,
        )

        # preate text Label props
        if font_family is not None:
            self._font_family = font_family
        if font_size is not None:
            self._font_size = font_size
        if text:
            self._text = text

        # setting font
        self._set_font()

        # setting the text color and the render
        if text_color is None:
            self._update_render()
        else:
            self.set_text_color(text_color)
        self.set_dimension()

    # getts and setters
    def _set_font(self):
        self._font = pygame.font.SysFont(
            self._font_family,
            self._font_size,
            True,
            False,
        )

    def _update_render(self):
        self._text_rendered = self._font.render(
            self._text,
            True,
            self.text_color
        )

    def set_text_color(self, value: tuple or list):
        if isinstance(value, pygame.Color):
            self.set_text_color = pygame.Color(*value)
            self._update_render()

    def set_dimension(self, value=None):
        if self._font is None:
            return

        if self._font is not None:
            super().set_dimension((self._font.size(self.text)))

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value: str):
        self._text = value
        self._update_render()
        self.set_dimension()

    @property
    def font_family(self):
        return self._font_family

    @font_family.setter
    def font_family(self, value: str):
        self._font_family = value
        self._set_font()
        self.set_dimension()

    @property
    def font_size(self):
        return self._font_size

    @font_size.setter
    def font_size(self, value: int):
        self._font_size = value
        self._update_render()
        self.set_dimension()

    # inherited
    def how_to_draw_me(self, screen):
        if self.parent is not None:
            super().how_to_draw_me(screen, draw_children=False)

        screen.blit(self._text_rendered, self.relative_pos)
