import pygame
pygame.init()

window_size = window_width, window_height = 800, 600
window_centre = window_width // 2, window_height // 2
window = pygame.display.set_mode(window_size)

colour = {'black': (0, 0, 0),
          'white': (255, 255, 255)}

state = 'main_menu'
