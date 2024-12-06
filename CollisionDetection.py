import pygame
import Sound

red = (255,0,0)    
blue = (0,0,255)

class AABB:
    def __init__(self, x, y, width, height, collision_enabled = True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.collision_enabled = collision_enabled
        self.color = red

    def get_bounds(self):
        x_min = self.x - self.width / 2
        x_max = self.x + self.width / 2
        y_min = self.y - self.height / 2
        y_max = self.y + self.height / 2
        return x_min, x_max, y_min, y_max
    
    def draw(self, screen):
        x_min, x_max, y_min, y_max = self.get_bounds()
        pygame.draw.rect(screen, self.color, (x_min, y_min, self.width, self.height), 2)

    def set_collision_enabled(self, enabled):
        self.collision_enabled = enabled

    
def is_colliding_aabb(rect1, rect2):
    r1_x_min, r1_x_max, r1_y_min, r1_y_max = rect1.get_bounds()
    r2_x_min, r2_x_max, r2_y_min, r2_y_max = rect2.get_bounds()
    collision = False
    rect1.color = red
    rect2.color = red

    # AABB 충돌 체크
    if(rect1.collision_enabled == False or rect2.collision_enabled == False):
        collision = False
    elif (r1_x_min < r2_x_max and r1_x_max > r2_x_min and
            r1_y_min < r2_y_max and r1_y_max > r2_y_min):
        collision = True
        rect1.color = blue
        rect2.color = blue


    return collision