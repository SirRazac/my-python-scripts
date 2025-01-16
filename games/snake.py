# ------------------------------------------------------------------------------ 
# Import Packages
# ------------------------------------------------------------------------------ 
import pygame
import random

pygame.init()

# Define screen size
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Starting position of snake
snake = [(100, 100), (80, 100), (60, 100)]
BLOCK_SIZE = 20
snake_dir = (BLOCK_SIZE, 0) # starts moving right

# Food position
food = (random.randint(0, (WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE,
        random.randint(0, (HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE)

score = 0
start_time = pygame.time.get_ticks()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # controlling snake
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != (0, BLOCK_SIZE): 
        snake_dir = (0, -20)  # up
    if keys[pygame.K_DOWN] and snake_dir != (0, -BLOCK_SIZE):
        snake_dir = (0, 20)  # down
    if keys[pygame.K_LEFT] and snake_dir != (BLOCK_SIZE, 0):
        snake_dir = (-20, 0)  # left
    if keys[pygame.K_RIGHT] and snake_dir != (-BLOCK_SIZE, 0):
        snake_dir = (20, 0)  # right
    
    # Snake movement
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])

    # Collision check with screen edges (wrap-around logic)
    if new_head[0] < 0:  # If the snake goes off the left side of the screen
        new_head = (WIDTH - BLOCK_SIZE, new_head[1])  # Appear on the right side
    elif new_head[0] >= WIDTH:  # If the snake goes off the right side of the screen
        new_head = (0, new_head[1])  # Appear on the left side

    if new_head[1] < 0:  # If the snake goes off the top side of the screen
        new_head = (new_head[0], HEIGHT - BLOCK_SIZE)  # Appear at the bottom
    elif new_head[1] >= HEIGHT:  # If the snake goes off the bottom side of the screen
        new_head = (new_head[0], 0)  # Appear at the top

    # End the game if snake collides with itself
    if new_head in snake:
        running = False  
    
    # Add the new head of the snake
    snake.insert(0, new_head)
    
    # Check if snake eats the food
    if new_head == food:
        score += 5  # Increment score
        food = (random.randint(0, (WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE,
                random.randint(0, (HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE)


    else:
        # Remove the last segment if no food was collected
        snake.pop()

    # Screen with backcolor
    screen.fill((255, 255, 255))  # white

    # Building snake
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, BLOCK_SIZE, BLOCK_SIZE))  # green

    # Drawing the food
    pygame.draw.rect(screen, (255, 0, 0), (*food, BLOCK_SIZE, BLOCK_SIZE))  # red
    
    # Calculate elapsed time
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # in seconds

    # Display score and elapsed time
    font = pygame.font.SysFont('Arial', 25)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    time_text = font.render(f"Time: {int(elapsed_time)}s", True, (0, 0, 0))

    screen.blit(score_text, (10, 10))  # Show score on the screen
    screen.blit(time_text, (WIDTH - 150, 10))  # Show time on the screen
    
    pygame.display.flip()
    clock.tick(15)

# game over screen
font = pygame.font.SysFont('Arial', 50)
game_over_text = font.render("Game Over!", True, (255, 0, 0))
score_text = font.render(f"Final Score: {score}", True, (0, 0, 0))

screen.fill((255, 255, 255))
screen.blit(game_over_text, (WIDTH // 3, HEIGHT // 3))
screen.blit(score_text, (WIDTH // 3, HEIGHT // 2))

pygame.display.flip()
pygame.time.wait(3000)

pygame.quit()