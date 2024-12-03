import pygame
import random

class Gift:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = 25

    def move(self):
        self.y -= self.speed
        if self.y < -self.radius:
            self.y = 600
            self.x = random.randint(50, 750)

    def draw(self, screen, image):
        screen.blit(image, (self.x - self.radius, self.y - self.radius))
