# ------------------------------------------------------------------------------ 
# Import Packages
# ------------------------------------------------------------------------------ 
import pygame

pygame.init()

# Define screen size
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Starting position of snake
snake = [(100, 100), (80, 100), (60, 100)]
BLOCK_SIZE = 20
snake_dir = (BLOCK_SIZE, 0) # starts moving right

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # controlling snake
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != (0, 20): 
        snake_dir = (0, -20)  # top
    if keys[pygame.K_DOWN] and snake_dir != (0, -20):
        snake_dir = (0, 20)  # bottom
    if keys[pygame.K_LEFT] and snake_dir != (20, 0):
        snake_dir = (-20, 0)  # left
    if keys[pygame.K_RIGHT] and snake_dir != (-20, 0):
        snake_dir = (20, 0)  # right
    
    new_head = (snake[0][0] + snake_dir[0], snake [0][1] + snake_dir[1])
    snake.insert(0, new_head) # adding new head
    snake.pop() # deleting last segment

    # Screen with backcolor
    screen.fill((255, 255, 255))  # white

    # Building snake
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, BLOCK_SIZE, BLOCK_SIZE))  # green

    pygame.display.flip()
    clock.tick(30)

pygame.quit()