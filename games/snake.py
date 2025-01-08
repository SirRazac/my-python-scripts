# ------------------------------------------------------------------------------
# Import Packages
# ------------------------------------------------------------------------------
import pygame

pygame.init()

# define screen size
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Screen with backcolor
    screen.fill((255, 255, 255)) # white
    pygame.display.flip()
    clock.tick(30)

pygame.quit()