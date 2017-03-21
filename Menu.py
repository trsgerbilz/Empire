import GlobalVar as Gbl
import pygame
import numpy as np
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


def render():
    Gbl.window.fill(Gbl.colour['white'])
    draw_text("Empire", 72, 100)  # ==Title==
    play_box = draw_box(-50, -25, 100, 50)  # ==Play Box==
    draw_text("Play", 46)  # ==Play==
    editor_box = draw_box(-65, 45, 130, 50)  # ==Editor Box==
    draw_text("Editor", 46, -70)
    settings_box = draw_box(-80, 115, 160, 50)  # ==Settings Box==
    draw_text("Settings", 46, -140)  # ==Settings==
    return play_box, editor_box, settings_box


def button_events(mouse_pos):
    """Handles mouse click button events"""
    if play_box.collidepoint(mouse_pos):
        print("Play")  # TODO return
    elif editor_box.collidepoint(mouse_pos):
        Gbl.state = 'editor'
    elif settings_box.collidepoint(mouse_pos):
        print("Settings")

play_box, editor_box, settings_box = render()

