import time

import pygame
import random
import math

pygame.init()


# Constants
NUM_PARTICLES = 100
PARTICLE_RADIUS = 5
PARTICLE_SPEED = 2
PARTICLE_COLLISION_DISTANCE = 2 * PARTICLE_RADIUS
BOUNDARY_WIDTH = 25
BACKGROUND_COLOR = (255, 255, 255)
PARTICLE_COLOR = (0, 0, 255)
BOUNDARY_COLOR = (23, 35, 200)
FONT_COLOR = (56, 130, 180)
FONT_ = pygame.font.Font(None, 25)


# Particle class
class Particle:
    def __init__(self):
        self.x = random.randint(BOUNDARY_WIDTH, 800 - BOUNDARY_WIDTH)
        self.y = random.randint(BOUNDARY_WIDTH, 600 - BOUNDARY_WIDTH)
        self.vx = random.uniform(-PARTICLE_SPEED, PARTICLE_SPEED)
        self.vy = random.uniform(-PARTICLE_SPEED, PARTICLE_SPEED)

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Handle collisions with boundaries
        if self.x < BOUNDARY_WIDTH or self.x > 800 - BOUNDARY_WIDTH:
            self.vx = -self.vx
        if self.y < BOUNDARY_WIDTH or self.y > 600 - BOUNDARY_WIDTH:
            self.vy = -self.vy

    def draw(self, screen):
        pygame.draw.circle(screen, PARTICLE_COLOR, (int(self.x), int(self.y)), PARTICLE_RADIUS)

    def collide(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance < PARTICLE_COLLISION_DISTANCE:
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

    def updateVelocity(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance < PARTICLE_COLLISION_DISTANCE:
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

            x = round(self.vx, 2)
            y = round(self.vy, 2)
            if round(self.vx, 2) > 0 or -0:
                if round(self.vy, 2) > 0 or -0:
                    return (self.vx, self.vy)
            else:
                return (random.uniform(0, 2), random.uniform(0, 2))
