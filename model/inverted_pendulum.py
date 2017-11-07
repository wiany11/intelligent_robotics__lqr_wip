from math import cos, sin


rod_len = 125

class Rod:
    
    def __init__(self, x, y):
        global rod_len
        
        self.rod_len = rod_len
        
        self.start_x = x
        self.start_y = y
        
        self.end_x = x
        self.end_y = y + self.rod_len
        
        self.theta = 0
    
        
    def change_theta(self, delta_theta):
        self.theta += delta_theta
        self.end_x = 1.0 * self.start_x + self.rod_len * sin(self.theta)
        self.end_y = 1.0 * self.start_y + self.rod_len * cos(self.theta)


    def set_theta(self, new_theta):
        self.theta = new_theta
        self.end_x = 1.0 * self.start_x + self.rod_len * sin(self.theta)
        self.end_y = 1.0 * self.start_y + self.rod_len * cos(self.theta)
       

class Wheel:
    
    def __init__(self, x, y):
        self.center_x = x
        self.center_y = y
        
        self.r = 25