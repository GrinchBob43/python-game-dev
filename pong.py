WHITE = 255, 255, 255

#define screen borders
winX = 800
winY = 590

import pygame

# Initialize Pygame 
pygame.init()

# Set up the display surface 
screen = pygame.display.set_mode((winX, winY))

# Set the window title
pygame.display.set_caption("Pong") 



# Game loop
running = True
while running:

  # Check for events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Draw background
  screen.fill((173, 216, 230))
  
    #draw  paddle

pygame.draw.rect(screen, WHITE, (100, 150, 250, 100))

  # Update display
 pygame.display.update()

# Quit Pygame  
pygame.quit()
