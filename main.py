import pygame
import sys
import config
import random
from boid import Boid

def main():
    pygame.init()

    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    pygame.display.set_caption("Boids")
    clock = pygame.time.Clock()

    flock = []

    #generez pozitiile initiale si le adaug in stol
    for _ in range(50):
        x = random.randint(0, config.SCREEN_WIDTH)
        y = random.randint(0, config.SCREEN_HEIGHT)
        flock.append(Boid(x, y))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(config.BG_COLOR)

        for boid in flock:
            boid.update(flock)
            boid.draw(screen)

        #actualizeaza ecranu
        pygame.display.flip()
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()