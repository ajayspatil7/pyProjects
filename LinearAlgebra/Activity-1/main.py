import pygame
import random
import math
import constants
from constants import Particle

# Set up Pygame
pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("N-Particle Simulation with Collision")


# Create particles
particles = []
for i in range(constants.PARTICLE_COUNT):
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
    pygame.draw.rect(screen, constants.BOUNDARY_COLOR, (0, 0, 1000, constants.WALL_WIDTH))  # Top
    pygame.draw.rect(screen, constants.BOUNDARY_COLOR, (0, 0, constants.WALL_WIDTH, 800))  # Left
    pygame.draw.rect(screen, constants.BOUNDARY_COLOR, (0, 800 - constants.WALL_WIDTH, 1000, constants.WALL_WIDTH))  # Bottom
    pygame.draw.rect(screen, constants.BOUNDARY_COLOR, (1000 - constants.WALL_WIDTH, 0, constants.WALL_WIDTH, 800))  # Right

    # Move and PARTICLE_BODY particles
    for particle in particles:
        particle.COLLISION()
        particle.PARTICLE_BODY(screen)

        # Check for collisions with other particles
        for other in particles:
            if particle != other:
                particle.COLLIDE(other)
                PARTICLE_COLOR = (0, 0, 0)

    travellingVelocity = constants.PARTICLE_INITIAL_VELOCITY
    if particle.UPDATE_VEL(other) >= 10:
        travellingVelocity = particle.UPDATE_VEL(other)
    else:
        travellingVelocity = 0

    # Some small Variables
    FONT_ = pygame.font.Font(None, 25)
    marker = "↑" if travellingVelocity > 0 else "↓"

    # Updates label
    INITIAL_VELOCITY = FONT_.render("Initial Set Velocity : " + str("±") + str(constants.PARTICLE_INITIAL_VELOCITY), True, constants.FONT_COLOR)
    AFTER_COLLISION = FONT_.render("Velocity after collision : " + str(particle.UPDATE_VEL(other)) + "m/s", True, constants.FONT_COLOR)
    FREE_MOVING_VELOCITY = FONT_.render("Particle Velocity : " + str(f"({particle.VELOCITY()})m/s"), True, constants.FONT_COLOR)
    PARTICLE_COUNT_LABEL = FONT_.render("Particle Count : " + str(constants.PARTICLE_COUNT), True, constants.FONT_COLOR)
    VEL_GAIN = FONT_.render("Velocity Gain : " + str(f"{particle.VELOCITY_GAIN(other)}m/s"), True, constants.FONT_COLOR)
    PARTICLE_RAD = FONT_.render("Particle Radius : " + str(constants.PARTICLE_RADIUS), True, constants.FONT_COLOR)

    # Draw label
    screen.blit(INITIAL_VELOCITY, (25, 25))
    screen.blit(PARTICLE_COUNT_LABEL, (25, 50))
    screen.blit(PARTICLE_RAD, (25, 75))

    screen.blit(VEL_GAIN, (25, 700))
    screen.blit(FREE_MOVING_VELOCITY, (25, 725))
    screen.blit(AFTER_COLLISION, (25, 750))

    # Update screen
    pygame.display.flip()
