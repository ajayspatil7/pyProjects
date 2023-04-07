import pygame
import random

# Set up Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Particle Animation")

# Constants
NUM_PARTICLES = 10
PARTICLE_RADIUS = 5
PARTICLE_SPEED = 10
BACKGROUND_COLOR = (255, 255, 255)
PARTICLE_COLOR = (235, 91, 187)
FONT_COLOR = (235, 91, 187)
FONT_COLOR_2 = (169, 123, 258)


class Particle:
    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.vx = random.uniform(-PARTICLE_SPEED, PARTICLE_SPEED)
        self.vy = random.uniform(-PARTICLE_SPEED, PARTICLE_SPEED)

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.x < 0 or self.x > 800:
            self.vx = -self.vx
        if self.y < 0 or self.y > 600:
            self.vy = -self.vy

    def draw(self, screen):
        pygame.draw.circle(screen, PARTICLE_COLOR, (int(self.x), int(self.y)), PARTICLE_RADIUS)


# Create particles
particles = []
for i in range(NUM_PARTICLES):
    particles.append(Particle())

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BACKGROUND_COLOR)
    font = pygame.font.Font(None, 30)

    # Move and draw particles
    for particle in particles:
        particle.move()
        particle.draw(screen)

    label = font.render("Particle Speed: " + str(PARTICLE_SPEED), True, FONT_COLOR)
    screen.blit(label, (10, 10))

    label2 = font.render("Particle count: " + str(NUM_PARTICLES), True, FONT_COLOR_2)
    screen.blit(label2, (10, 35))

    # Update screen
    pygame.display.flip()

# Clean up
pygame.quit()
