import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball parameters
ball_radius = 25
ball_x = (screen_width - ball_radius) // 2
ball_y = (screen_height - ball_radius) // 2
ball_speed = 20
 
# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    # Get the state of all keyboard buttons
    keys = pygame.key.get_pressed()
 
    # Move the ball based on pressed keys
    if keys[pygame.K_UP]:
        ball_y -= ball_speed
    if keys[pygame.K_DOWN]:
        ball_y += ball_speed
    if keys[pygame.K_LEFT]:
        ball_x -= ball_speed
    if keys[pygame.K_RIGHT]:
        ball_x += ball_speed
 
    # Keep the ball within the screen bounds
    ball_x = max(ball_radius, min(screen_width - ball_radius, ball_x))
    ball_y = max(ball_radius, min(screen_height - ball_radius, ball_y))
 
    # Clear the screen
    screen.fill(WHITE)
 
    # Draw the ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
 
    # Update the display
    pygame.display.flip()
 
# Quit Pygame
pygame.quit()
sys.exit()