import math
import pygame
import random
import tkinter as tk
from tkinter import messagebox
pygame.init()
win=pygame.display.set_mode((500,500))
win.fill((255,255,255))

class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 40)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
def redrawwindow():
    win.fill((255,255,255))
    game.draw(win,(0,0,0))
    option.draw(win,(0,0,0))
def ption():
    pass
def ame():
    print("1")
run=True
game=button((0,255,0),15,50,250,100,"Play Game")
option=button((0,255,0),15,200,250,100,"options")
while run:
    redrawwindow()
    pygame.display.update()
    for event in pygame.event.get():
        pos=pygame.mouse.get_pos()
        if event.type==pygame.QUIT:
            run=False
            pygame.quit
            quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if game.isOver(pos):
                ame()
            if option.isOver(pos):
                ption()
        if event.type==pygame.MOUSEMOTION:
            if game.isOver(pos):
                game.color=(255,0,0)
            else:
                game.color=(0,255,0)
            if option.isOver(pos):
                option.color=(255,0,0)
            else:
                option.color=(0,255,0)