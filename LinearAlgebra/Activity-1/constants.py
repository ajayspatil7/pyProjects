import time
import pygame
import random
import math

pygame.init()

# Particle Constants
PARTICLE_COUNT = 20
PARTICLE_RADIUS = 5
PARTICLE_INITIAL_VELOCITY = 10
# Collision Constants
COLL_DIST = 2 * PARTICLE_RADIUS
WALL_WIDTH = 20
# Window Constants
BACKGROUND_COLOR = (255, 255, 255)
PARTICLE_COLOR = (0, 0, 0)
BOUNDARY_COLOR = (242, 58, 66)
FONT_COLOR = (56, 130, 180)
FONT_ = pygame.font.Font(None, 25)


# Particle class
class Particle:
    def __init__(self):
        self.x = random.randint(WALL_WIDTH, 1000 - WALL_WIDTH)
        self.y = random.randint(WALL_WIDTH, 800 - WALL_WIDTH)
        self.vx = random.uniform(-PARTICLE_INITIAL_VELOCITY, PARTICLE_INITIAL_VELOCITY)
        self.vy = random.uniform(-PARTICLE_INITIAL_VELOCITY, PARTICLE_INITIAL_VELOCITY)

    def COLLISION(self):
        self.x += self.vx
        self.y += self.vy

        # Handle collisions with boundaries
        if self.x < WALL_WIDTH or self.x > 1000 - WALL_WIDTH:
            self.vx = -self.vx
        if self.y < WALL_WIDTH or self.y > 800 - WALL_WIDTH:
            self.vy = -self.vy

    def PARTICLE_BODY(self, screen):
        pygame.draw.circle(screen, PARTICLE_COLOR, (int(self.x), int(self.y)), PARTICLE_RADIUS)

    def COLLIDE(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance < COLL_DIST:
            angle = math.atan2(dy, dx)
            sin_angle = math.sin(angle)
            cos_angle = math.cos(angle)

            # Rotate velocities
            vx1 = self.vx * cos_angle - self.vy * sin_angle
            vy1 = self.vx * sin_angle + self.vy * cos_angle
            vx2 = other.vx * cos_angle - other.vy * sin_angle
            vy2 = other.vx * sin_angle + other.vy * cos_angle

            # Update velocities
            self.vx = vx2 * cos_angle + vy1 * sin_angle
            self.vy = vy1 * cos_angle - vx2 * sin_angle
            other.vx = vx1 * cos_angle + vy2 * sin_angle
            other.vy = vy2 * cos_angle - vx1 * sin_angle

    def UPDATE_VEL(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance < COLL_DIST:
            angle = math.atan2(dy, dx)
            sin_angle = math.sin(angle)
            cos_angle = math.cos(angle)

            # Rotate velocities
            vx1 = self.vx * cos_angle - self.vy * sin_angle
            vy1 = self.vx * sin_angle + self.vy * cos_angle
            vx2 = other.vx * cos_angle - other.vy * sin_angle
            vy2 = other.vx * sin_angle + other.vy * cos_angle

            # Update velocities
            self.vx = vx2 * cos_angle + vy1 * sin_angle
            self.vy = vy1 * cos_angle - vx2 * sin_angle
            other.vx = vx1 * cos_angle + vy2 * sin_angle
            other.vy = vy2 * cos_angle - vx1 * sin_angle

            if vx1 - vy2 and vx2 - vy1 > 0:
                return round(vx1 - vy2, 2)
            else:
                return 0
