import pygame
import sys

# Initialize Pygame
pygame.init()


# Set up display
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")


# Main loop
while True:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()


  window.fill((0, 0, 0))  # Fill the screen with black
  pygame.display.flip()  # Update the display
