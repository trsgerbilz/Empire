import pygame
import numpy as np
pygame.init()

pygame.display.set_caption('Empire')
window_size = window_width, window_height = 800, 600
window_centre = window_width // 2, window_height // 2
window = pygame.display.set_mode(window_size)

black = 0, 0, 0
white = 255, 255, 255

state = 'main_menu'

window_clock = pygame.time.Clock()


class State:
    def __init__(self):
        global state
        self.state = state
        MainMenu().render()

    def main_menu(self):
        MainMenu().render()
        self.state = 'main_menu'

        """
        elif state == 'play':
            pass  # todo play screen
        elif state == 'editor':
            pass  # todo editor screen
        elif state == 'settings':
            pass  # todo settings screen
        """


class MainMenu:
    def __init__(self):
        self.play_box = self.draw_box(-50, -25, 100, 50)
        self.editor_box = self.draw_box(-65, 45, 130, 50)
        self.settings_box = self.draw_box(-80, 115, 160, 50)

    def draw_text(self, content, size, height=0):
        font = pygame.font.SysFont('', size)
        text = font.render(content, True, black)
        text_centre = text.get_width() // 2, text.get_height() // 2 + height
        text_pos = np.subtract(window_centre, text_centre)
        window.blit(text, text_pos)

    def draw_box(self, xpos, ypos, xsize, ysize):
        box_rect = pygame.Rect(window_centre[0] + xpos, window_centre[1] + ypos, xsize, ysize)
        pygame.draw.rect(window, black, box_rect, 7)
        return box_rect

    def render(self):
        window.fill(white)
        self.draw_text("Empire", 72, 100)  # ==Title==
        self.play_box = self.draw_box(-50, -25, 100, 50)  # ==Play Box==
        self.draw_text("Play", 46)  # ==Play==
        self.editor_box = self.draw_box(-65, 45, 130, 50)  # ==Editor Box==
        self.draw_text("Editor", 46, -70)
        self.settings_box = self.draw_box(-80, 115, 160, 50)  # ==Settings Box==
        self.draw_text("Settings", 46, -140)  # ==Settings==

    def button_events(self, mouse_pos):
        """Handles mouse click button events"""
        if self.play_box.collidepoint(mouse_pos):
            print("Play")
        elif self.editor_box.collidepoint(mouse_pos):
            print("Editor")
        elif self.settings_box.collidepoint(mouse_pos):
            print("Settings")


class Editor:
    def draw_text(self, content, size, height=0):
        font = pygame.font.SysFont('', size)
        text = font.render(content, True, black)
        text_centre = text.get_width() // 2, text.get_height() // 2 + height
        text_pos = np.subtract(window_centre, text_centre)
        window.blit(text, text_pos)

    def draw_box(self, xpos, ypos, xsize, ysize):
        box_rect = pygame.Rect(window_centre[0] + xpos, window_centre[1] + ypos, xsize, ysize)
        pygame.draw.rect(window, black, box_rect, 7)
        return box_rect

    def toolbar(self):
        pygame.image.load("Icons/add.png")


class LeftMouseEvents:
    def __init__(self):
        global state
        self.state = state

        if state == 'main_menu':
            MainMenu().button_events(pygame.mouse.get_pos())


def main():
    """main"""

    State()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                LeftMouseEvents()

        pygame.display.update()
        window_clock.tick(60)

main()
