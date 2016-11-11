import pygame
from pygame.locals import *

class Background:

    def __init__(self, size, color, img):
        self.size = size
        self.color = color
        self.img = img
        self.screen = pygame.display.set_mode(self.size)
        self.font = pygame.image.load(self.img).convert()
        pygame.display.set_caption("Test")

    def drawBgColor(self):
        self.screen.fill(self.color)

    def setBgImg(self,img):

        self.img = img
        self.font = pygame.image.load(img).convert()

    def drawBgImg(self):
        self.screen.blit(self.font, (0,0,self.size[0], self.size[1]))


class Node:

    def __init__(self, size, img):
        self.x = size[0]/2
        self.y = size[1]/2
        self.surface = pygame.Surface((30,30))
        self.w = self.h = 30
        self.img = pygame.image.load(img).convert_alpha()
        self.color = (100,100,100)
        self.stepX = self.stepY = 3

    def collisionX(self, limit):
        if((self.x < 0) or (self.x + self.w > limit)):
            return True
        return False

    def collisionY(self, limit):
        if((self.y < 0) or (self.y + self.h > limit)):
            return True
        return False

    def collision(self, anotherObject, limitx, limity):
        if(anotherObject == True):
            self.stepX = -self.stepX
        if(self.collisionX(limitx) == True):
            self.stepX = -self.stepX
        if(self.collisionY(limity) == True):
            self.stepY = -self.stepY

    def moveOn(self):
        self.x += self.stepX
        self.y += self.stepY

    def drawNodeRect(self, screen):
        pygame.draw.rect(screen,self.color,[self.x,self.y,self.h,self.w],0)

    def drawNodeImg(self, screen):
        screen.blit(self.img,(self.x,self.y))


class Paddle:

    def __init__(self, winSize, size, player):
        if(player == 0):
            self.x = 0
        else:
            self.x = winSize[0]-size[0]

        self.y     = (winSize[1]-size[1])/2
        self.size  = size
        self.up    = 0
        self.down  = 0
        self.color = (0,255,0)

    def getEvent(self, event):
        if event.type == KEYDOWN:
            if event.key == K_UP:
                self.up = 1
                return True
            if event.key == K_DOWN:
                self.down = 1
                return True
            return True
        if event.type == KEYUP:
            if event.key == K_UP:
                self.up = 0
                return True
            if event.key == K_DOWN:
                self.down = 0
                return True

    def moveOn(self, winSize):
        if(self.up == 1):
            if(self.y <= 0):
                return True
            self.y -= 5
            return True
        if(self.down == 1):
            if(self.y + self.size[1] >= winSize[1]):
                return True
            self.y += 5

    def tracking(self, target):
        if(target.y + target.h < self.y):
            self.up   = 1
            self.down = 0
            return True
        if(target.y > self.y + self.size[1]):
            self.up   = 0
            self.down = 1

    def targetCollision(self, target):
        if(self.y > target.y + target.h):
            return False
        if(target.y > self.y + self.size[1]):
            return False
        if(self.x > target.x + target.w):
            return False
        if(target.x > self.x + self.size[0]):
            return False
        return True

    def drawPaddleRect(self, screen):
        pygame.draw.rect(screen,self.color,[self.x,self.y,self.size[0],self.size[1]],0)

class Score:

    def __init__(self):
        self.score = 0
        pygame.font.init()

    def plusOne(self):
        self.score += 1

    def reset(self):
        self.score = 0

    def draw(self,screen):
        font = pygame.font.Font(None, 36)
        text = font.render("Score: "+ str(self.score), 1, (0, 255, 0))
        textpos = text.get_rect()
        textpos.centerx = screen.get_rect().centerx
        screen.blit(text, textpos)
