from utils.game import Game
from utils.window import Window
import pygame
from pygame import QUIT
import sys


class Main:

    def __init__(self):
        labyrinth = Game("sample_map.txt")
        window = Window(labyrinth)
        labyrinth.window = window
        while True:  # main game loop
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        window.player.move_left()
                        labyrinth.move('l')
                    if event.key == pygame.K_RIGHT:
                        window.player.move_right()
                        labyrinth.move('r')
                    if event.key == pygame.K_DOWN:
                        window.player.move_down()
                        labyrinth.move('d')
                    if event.key == pygame.K_UP:
                        window.player.move_up()
                        labyrinth.move('u')
            if labyrinth.state == "win" or labyrinth.state == "lose":
                window.message_display("You {}!".format(labyrinth.state))
            else:
                window.refresh()


if __name__ == "__main__":
    Main()
