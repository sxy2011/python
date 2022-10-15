import pygame


class game:
    def __init__(self):
        WIDTH, HEIGHT = 800, 500
        WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    def main(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

        pygame.quit()

        return 1


me = game()
me.main()
