import pygame
import random


class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 7
        self.score = 0

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        '''
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.y > 10:
            self.y -= self.vel
        if keys[pygame.K_DOWN] and self.y + self.height < 590:
            self.y += self.vel
        '''
        mouse_y = pygame.mouse.get_pos()[1] - self.height/2
        if self.y < mouse_y and self.y + self.height < 590:
                self.y += self.vel
        
        if self.y > mouse_y and self.y > 10 :
            self.y -= self.vel
        
        self.update()


class Ball():
    def __init__(self, width, height, rad, color):
        self.width = width
        self.height = height
        self.rad = rad
        self.color = color
        self.x = width/2
        self.y = height/2
        self.rect = (self.x, self.y, self.rad, self.rad)
        self.vel_x = 3 * random.choice([-1, 1])
        self.vel_y = 3 * random.choice([-1, 1])
        self.p1_score = 0
        self.p2_score = 0

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.rad)

    def update(self):
        self.rect = (self.x, self.y, self.rad, self.rad) 

    def move(self, p1, p2):
        self.x += self.vel_x
        self.y += self.vel_y

        if self.y >= self.height:
            self.vel_y *= -1

        if self.y <= 0:
            self.vel_y *= -1

        if self.x > self.width or self.x < 0:
            self.x = self.width / 2
            self.y = self.height / 2
            self.vel_x *= random.choice([-1, 1])
            self.vel_y *= random.choice([-1, 1])
    
        if self.x - 10 <= p1.x + p1.width and self.x - 10 >= p1.x:
            if self.y >= p1.y and self.y <= p1.y + p1.height:
                self.vel_x *= -1

        if self.x + 10 >= p2.x and self.x + 10 <= p2.x + p2.width:
            if self.y >= p2.y and self.y <= p2.y + p2.height:
                self.vel_x *= -1

        self.score()

        self.update()

        return self

    def score(self):
        if self.x <= 0:  
            self.p2_score += 1
        elif self.x >= self.width:
            self.p1_score += 1 



        
            
            
