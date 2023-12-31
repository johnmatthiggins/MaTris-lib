#!/usr/bin/env python
import pygame

from matris import Game
from matris import create_screen

def main():
    screen = create_screen()
    game = Game(screen)

    while game.step():
        pass

if __name__ == "__main__":
    main()
