# standards
import math

# third party
import pygame


def triangle(center, size, old_triangle=None) -> tuple:
    # thirty degrees
    td = math.pi / 6

    x = size * math.sin(td)
    y = size * math.cos(td)

    if(old_triangle is None):
        old_triangle = (pygame.Vector2(), pygame.Vector2(), pygame.Vector2())

    aux = round(center[1] + y)
    old_triangle[0].x = round(center[0] - x)
    old_triangle[0].y = aux
    old_triangle[1].x = round(center[0] + x)
    old_triangle[1].y = aux
    old_triangle[2].x = round(center[0])
    old_triangle[2].y = round(center[1] - y)

    return old_triangle


def triangle_rotate(angle, triangle):
    pass
