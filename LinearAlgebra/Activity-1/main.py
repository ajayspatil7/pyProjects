import pygame
import random
import math
import constants
from constants import Particle

# Set up Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Particle Animation")


# Create particles
particles = []
for i in range(constants.NUM_PARTICLES):
    particles.append(Particle())

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(constants.BACKGROUND_COLOR)

    # Draw boundaries
    pygame.draw.rect(screen, constants.BOUNDARY_COLOR, (0, 0, 800, constants.BOUNDARY_WIDTH))  # Top
    pygame.draw.rect(screen, constants.BOUNDARY_COLOR, (0, 0, constants.BOUNDARY_WIDTH, 600))  # Left
    pygame.draw.rect(screen, constants.BOUNDARY_COLOR, (0, 600 - constants.BOUNDARY_WIDTH, 800, constants.BOUNDARY_WIDTH))  # Bottom
    pygame.draw.rect(screen, constants.BOUNDARY_COLOR, (800 - constants.BOUNDARY_WIDTH, 0, constants.BOUNDARY_WIDTH, 600))  # Right

    # Move and draw particles
    for particle in particles:
        particle.move()
        particle.draw(screen)

        # Check for collisions with other particles
        for other in particles:
            if particle != other:
                particle.collide(other)
    FONT_ = pygame.font.Font(None, 25)

    # Update label
    label = FONT_.render("Particle Speed: " + str(particle.updateVelocity(other)), True, constants.FONT_COLOR)

    # Draw label
    screen.blit(label, (25, 25))

    # Update screen
    pygame.display.flip()
