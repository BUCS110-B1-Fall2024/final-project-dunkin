import pygame
import random
from src.item import Item
from src.gift import Gift

class GameController:
    def __init__(self, screen):
        self.screen = screen
        self.score = 10
        self.items = []
        self.gift = Gift(random.randint(50, 750), 600, 3)
        self.time_elapsed = 0

    def add_items(self, images):
        for _ in range(7):
            type = random.choice(["donut", "bread", "fork", "knife"])
            effect = 1 if type == "donut" else 2 if type == "bread" else -1 if type == "fork" else -2
            self.items.append(Item(random.randint(50, 750), random.randint(50, 550), random.randint(2, 5), type, effect))

    def update(self):
        for item in self.items:
            item.move()
        self.gift.move()

    def render(self, images, gift_image):
        for item in self.items:
            item.draw(self.screen, images)
        self.gift.draw(self.screen, gift_image)

    def handle_click(self, pos):
        for item in self.items[:]:
            if (item.x - pos[0]) ** 2 + (item.y - pos[1]) ** 2 < item.radius ** 2:
                self.score += item.effect
                self.items.remove(item)

        if (self.gift.x - pos[0]) ** 2 + (self.gift.y - pos[1]) ** 2 < self.gift.radius ** 2:
            self.score += random.choice([-5, 5])
            self.gift = Gift(random.randint(50, 750), 600, 3)
