# src/traffic_light.py
class TrafficLight:
    def __init__(self, x, y, color="red"):
        """신호등 초기화"""
        self.position = (x, y)  
        self.color = color  

    def change_color(self):
        """신호등 색상 변경"""
        if self.color == "red":
            self.color = "green"
        elif self.color == "green":
            self.color = "yellow"
        elif self.color == "yellow":
            self.color = "red"
