import Menu
import GlobalVar as Gbl
import Editor
import pygame

pygame.init()
pygame.display.set_caption('Empire')
window_clock = pygame.time.Clock()


def check_state():
    if Gbl.state == 'main_menu':
        Menu.render()

    elif Gbl.state == 'editor':
        Editor.render()

        """
        elif state == 'play':
            pass  # todo play screen

        elif state == 'settings':
            pass  # todo settings screen
        """


def left_mouse_events():
    if Gbl.state == 'main_menu':
        Menu.button_events(pygame.mouse.get_pos())
    elif Gbl.state == 'editor':
        Editor.button_events(pygame.mouse.get_pos())


def main():

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                left_mouse_events()

        check_state()
        pygame.display.update()
        window_clock.tick(60)

main()
