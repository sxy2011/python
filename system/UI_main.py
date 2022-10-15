import sys

import pygame


class game:
    def __init__(self):
        global WIN, WHITE
        WIDTH, HEIGHT = 800, 500
        WHITE = (255, 255, 255)
        pygame.init()
        WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('sxy system')

    def main(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.draw_window()
        sys.exit()

    def draw_window(self):
        WIN.fill(WHITE)
        pygame.display.update()

me = game()
me.main()
