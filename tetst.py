import pygame

# Initialize Pygame
pygame.init()

# Set the window size
screen = pygame.display.set_mode((400, 300))

# Create the ellipse shape
ellipse = pygame.Surface((100, 50))
ellipse.fill((255, 255, 255))
pygame.draw.ellipse(ellipse, (0, 0, 0), (0, 0, 100, 50))

# Rotate the ellipse by 45 degrees
ellipse = pygame.transform.rotate(ellipse, 45)

# Blit the ellipse to the screen
screen.blit(ellipse, (150, 100))

# Update the display
pygame.display.update()

# Wait for the user to close the window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
