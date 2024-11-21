# src/car.py
class Car:
    def __init__(self, x, y, speed=5):
        """차량 초기화"""
        self.position = [x, y]  
        self.speed = speed  

    def move(self, traffic_light_color):
        """신호등 색상에 따라 차량 이동"""
        if traffic_light_color == "green":
            self.position[0] += self.speed 
        elif traffic_light_color == "red":
            self.speed = 0  
