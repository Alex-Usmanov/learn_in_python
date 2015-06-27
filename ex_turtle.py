# coding:utf-8
import turtle
import math
from math import *
from random import randint

import pygame
from pygame.locals import *

# input()
'''
t.forward(100)
t.left(90)
t.right(90)
它默认出来是朝右的，你用这3个函数，画一个高200， 宽100的矩形

'''

t = turtle.Turtle()
color = (141 / 255.0, 218 / 255.0, 247 / 255.0)


def test1():
    t = turtle.Turtle()
    # input()
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(200)

    turtle.done()
    # 记得文件最后要有一个tuttle.done()，不然窗口直接就结束了


'''
def draw_rect(x,y,w,h):
    t=turtle.Turtle()
    t.penup()
    t.forward(x)
    t.right(90)
    t.forward(y)
    t.pendown()
    # t.right(90)
    t.left(90)

    t.forward(w)
    t.right(90)
    t.forward(h)
    t.right(90)
    t.forward(w)
    t.right(90)
    t.forward(h)

    t.penup()
    t.forward(y+h)
    t.left(90)
    t.forward(x+w)
    t.right(90)
    t.pendown()

    # turtle.done()
'''


def draw_rect(x, y, w, h, col=color):
    t.penup()
    t.forward(x)
    t.left(90)
    t.forward(y)

    t.pencolor(col)
    t.fillcolor(col)

    t.begin_fill()

    t.pendown()
    t.forward(h)
    t.right(90)
    t.forward(w)
    t.right(90)
    t.forward(h)
    t.right(90)
    t.forward(w)

    t.end_fill()

    t.penup()
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.left(90)


# '''

def draw_rect2(x, y, w, h, col=color):
    t.penup()
    t.goto(x, y)

    t.pendown()

    t.pencolor(col)
    t.fillcolor(col)

    t.begin_fill()
    t.goto(x, y + h)
    t.goto(x + w, y + h)
    t.goto(x + w, y)
    t.goto(x, y)
    t.end_fill()

    t.penup()


def draw_bar_chart(list):
    xi = 10
    yi = 10
    gap = 20
    # w=20
    for i in list:
        x = xi
        y = yi
        w = 20
        h = i * 30
        xi += gap + w
        # draw_rect(x,y,w,h)
        draw_rect2(x, y, w, h)


def draw_line_chart(list):
    xi = 10
    yi = 10
    gap = 20
    # w=20
    t.penup()
    # t.pendown()
    t.pencolor(color)
    for i in list:
        x = xi
        y = yi
        w = 20
        h = i * 30
        xi += gap + w

        t.goto(x + w / 2, y + h)
        if not t.isdown():
            t.pendown()
            # 这样是确保第一个点和起始位置之间不要有线条


def draw_circle(r, position=(0.0, 0.0)):
    t.penup()
    # x,y=pos
    for i in range(360):
        x = position[0] + r * cos(i / 180.0 * pi)
        y = position[1] + r * sin(i / 180.0 * pi)
        t.goto(x, y)
        # t.goto(x+r*cos(i/180.0*pi),y+r*sin(i/180.0*pi))
        if not t.isdown():
            t.pendown()
    t.penup()

def draw_sector(radius,start_angel,end_angel,position=(0.0,0.0),color=color):
    t.penup()
    x,y=position
    t.goto(x,y)

    t.pendown()
    start_angel=int(start_angel)
    end_angel=int(end_angel)
    for i in range(start_angel,end_angel):
        x=position[0]+radius*cos(i/180.0 * pi)
        y=position[1]+radius*sin(i/180.0 * pi)
        t.goto(x,y)
    t.goto(position[0],position[1])
    t.penup()

def random_color():
    return (randint(0,255)/255.0,randint(0,255)/255.0,randint(0,255)/255.0)

def draw_pie_chart(list,radius=50,position=(0.0,0.0)):
    gross=sum(list)
    precision=100 #Accurate to double digits
    t.penup()
    x,y=position
    marked_sector=0
    t.pendown()
    for sector in list:
        sector_color=random_color()
        t.pencolor(sector_color)
        t.fillcolor(sector_color)
        t.begin_fill()
        t.goto(position[0],position[1])
        for i in range(marked_sector*precision,(marked_sector+sector)*precision):
            x=position[0]+radius*cos(i/float(gross)/precision*pi*2)
            y=position[1]+radius*sin(i/float(gross)/precision*pi*2)
            t.goto(x,y)
        t.goto(position[0],position[1])
        t.end_fill()
        marked_sector+=sector
    # t.goto(position[0],position[1])
    t.penup()



if __name__ == '__main__':
    # test1()
    # draw_rect(10,30,300,40)
    list=[5,3,8,6]
    # draw_bar_chart(list)
    # draw_line_chart(list)
    # draw_circle(20)
    # draw_circle(40, (40.0, 50.0))
    # draw_circle(50, (60.0, 80.0))
    draw_sector(30,230,354,(80.0,80.0))
    draw_pie_chart(list)
    turtle.done()
