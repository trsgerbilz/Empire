import pygame
import numpy as np
pygame.init()

pygame.display.set_caption('Empire')
window_size = window_width, window_height = 800, 600
window_centre = window_width // 2, window_height // 2
window = pygame.display.set_mode(window_size)

menu_state = 'main'  # main, play, editor, settings

black = 0, 0, 0
white = 255, 255, 255

window_clock = pygame.time.Clock()


class MainMenu:
    def __init__(self):
        self.play_box = self.draw_box(-50, -25, 100, 50)
        self.editor_box = self.draw_box(-65, 45, 130, 50)
        self.settings_box = self.draw_box(-80, 115, 160, 50)

    def draw_text(self, text, size, height=0):
        font = pygame.font.SysFont('', size)
        text = font.render(text, True, black)
        text_centre = text.get_width() // 2, text.get_height() // 2 + height
        text_pos = np.subtract(window_centre, text_centre)
        window.blit(text, text_pos)

    def draw_box(self, xpos, ypos, xsize, ysize):
        box_rect = pygame.Rect(window_centre[0] + xpos, window_centre[1] + ypos, xsize, ysize)
        pygame.draw.rect(window, black, box_rect, 7)
        return box_rect

    def main_menu_render(self):
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


def main():
    """main"""

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                MainMenu().button_events(pygame.mouse.get_pos())  # todo this needs a better handler

        if menu_state == 'main':
            MainMenu().main_menu_render()
        elif menu_state == 'play':
            pass  # todo play screen
        elif menu_state == 'editor':
            pass  # todo editor screen
        elif menu_state == 'settings':
            pass  # todo settings screen

        pygame.display.update()
        window_clock.tick(60)

main()
