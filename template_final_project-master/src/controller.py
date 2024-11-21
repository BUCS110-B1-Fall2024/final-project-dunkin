# src/controller.py
import pygame
from src.traffic_light import TrafficLight
from src.car import Car

class Controller:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True

        # 객체 생성
        self.traffic_light = TrafficLight(300, 200, "red")
        self.car = Car(100, 300)

    def mainloop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.traffic_light.change_color()

          
            self.car.move(self.traffic_light.color)

          
            self.screen.fill((255, 255, 255))  
            pygame.draw.rect(self.screen, (255, 0, 0), (self.car.position[0], self.car.position[1], 50, 30)) 
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
