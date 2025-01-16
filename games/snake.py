# ------------------------------------------------------------------------------ 
# Import Packages
# ------------------------------------------------------------------------------ 
import pygame
import random

# ------------------------------------------------------------------------------ 
# Game
# ------------------------------------------------------------------------------
pygame.init()

# Define screen size
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BLOCK_SIZE = 20
FPS = 15

def start_game():
    # Starting position of snake
    snake = [(100.0, 100.0), (80.0, 100.0), (60.0, 100.0)]
    snake_dir = (BLOCK_SIZE, 0)  # starts moving right

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # ESC for quitting
                    running = False
            
        # controlling snake
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and snake_dir != (0, BLOCK_SIZE): 
            snake_dir = (0, -BLOCK_SIZE)  # up
        if keys[pygame.K_DOWN] and snake_dir != (0, -BLOCK_SIZE):
            snake_dir = (0, BLOCK_SIZE)  # down
        if keys[pygame.K_LEFT] and snake_dir != (BLOCK_SIZE, 0):
            snake_dir = (-BLOCK_SIZE, 0)  # left
        if keys[pygame.K_RIGHT] and snake_dir != (-BLOCK_SIZE, 0):
            snake_dir = (BLOCK_SIZE, 0)  # right
        
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
            score += 5 
            food = (random.randint(0, (WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE,
                    random.randint(0, (HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE)
        else:
            # Remove the last segment if no food was collected
            snake.pop()

        # Screen with background color
        screen.fill((255, 255, 255))

        # Building snake
        for segment in snake:
            pygame.draw.rect(screen, (0, 255, 0), (*segment, BLOCK_SIZE, BLOCK_SIZE))

        # Drawing the food
        pygame.draw.rect(screen, (255, 0, 0), (*food, BLOCK_SIZE, BLOCK_SIZE))

        # Calculate elapsed time
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # in seconds

        # Display score and elapsed time
        font = pygame.font.SysFont('Arial', 25)
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        time_text = font.render(f"Time: {int(elapsed_time)}s", True, (0, 0, 0))

        screen.blit(score_text, (10, 10))  # Show score on the screen
        screen.blit(time_text, (WIDTH - 150, 10))  # Show time on the screen

        pygame.display.flip()
        clock.tick(FPS)

    # Game Over screen
    game_over_screen(score)

# Game over screen with options
def game_over_screen(score):
    font = pygame.font.SysFont('Arial', 35)
    
    # Game Over Text
    game_over_text = font.render("Game Over!", True, (255, 0, 0))
    score_text = font.render(f"Final Score: {score}", True, (0, 0, 0))

    # Position text centrally
    game_over_text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    score_text_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    screen.fill((255, 255, 255))  # white background
    screen.blit(game_over_text, game_over_text_rect)
    screen.blit(score_text, score_text_rect)

    # Restart and Quit Text
    restart_text = font.render("Press R to Restart or Q to Quit", True, (0, 0, 0))
    restart_text_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 1.5))
    screen.blit(restart_text, restart_text_rect)

    pygame.display.flip()

    # Wait for player input to either restart or quit
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart the game
                    start_game()
                    waiting_for_input = False
                if event.key == pygame.K_q:  # Quit the game
                    pygame.quit()
                    exit()

# Start the game
start_game()

