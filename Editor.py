import GlobalVar as Gbl
import numpy as np
import pygame
pygame.init()


def draw_text(content, size, height=0):
    font = pygame.font.SysFont('', size)
    text = font.render(content, True, Gbl.colour['black'])
    text_centre = text.get_width() // 2, text.get_height() // 2 + height
    text_pos = np.subtract(Gbl.window_centre, text_centre)
    Gbl.window.blit(text, text_pos)


def draw_box(xpos, ypos, xsize, ysize):
    box_rect = pygame.Rect(Gbl.window_centre[0] + xpos, Gbl.window_centre[1] + ypos, xsize, ysize)
    pygame.draw.rect(Gbl.window, Gbl.colour['black'], box_rect, 7)
    return box_rect


def toolbar():
    pass
    # add_icon = pygame.image.load("Icons/add.png")


def render():
    Gbl.window.fill(Gbl.colour['white'])
    menu_box = draw_box(-50, -25, 100, 50)  # ==Menu Box==
    draw_text("Menu", 46)  # ==Menu==
    return menu_box


def button_events(mouse_pos):
    """Handles mouse click button events"""
    if menu_box.collidepoint(mouse_pos):
        Gbl.state = "main_menu"


menu_box = render()
