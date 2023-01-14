import pygame_menu
from pygame_menu.examples import create_example_window

from typing import Tuple, Any

surface = create_example_window('Example - Simple', (1000, 700))

def start_the_game() -> None:
    """
    Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc.
    """

menu = pygame_menu.Menu(
    height=400,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Welcome',
    width=500
)

menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(surface)