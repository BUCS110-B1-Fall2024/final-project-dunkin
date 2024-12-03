import random

class Item:
    def __init__(self, x, y, speed, type, effect):
        self.x = x
        self.y = y
        self.speed = speed
        self.type = type
        self.effect = effect
        self.radius = 25

    def move(self):
        self.y -= self.speed
        if self.y < -self.radius:
            self.y = 600
            self.x = random.randint(50, 750)

    def draw(self, screen, images):
        screen.blit(images[self.type], (self.x - self.radius, self.y - self.radius))

