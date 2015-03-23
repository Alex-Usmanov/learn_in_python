# -*- coding:utf-8 -*-
class Canvas():
    def __init__(self, width=100, height=100, clearChar=' ', pixelChar='*'):
        self.width = width
        self.height = height
        self.clearChar = clearChar
        self.pixelChar = pixelChar
        self.initCanvas()

    def initCanvas(self):
        self.canvas = [[self.clearChar] * self.width for i in range(self.height)]

    def display(self):
        for i in self.canvas:
            print ''.join(i)

    def drawPixel(self, x, y):
        # lack of validation
        self.canvas[y][x] = self.pixelChar


c = Canvas()

drawPixel = c.drawPixel


def drawLine(x1, y1, x2, y2):
    if x1 is x2:
        for i in range(y2 - y1 + 1):
            drawPixel(x1, y1 + i)
    elif y1 is y2:
        for i in range(x2-x1+1):
            drawPixel(x1+i,y1)
    else:
        k=(y2-y1)/(x2-x1)
        d=(y1*x2-y2*x1)/(x2-x1)
        for i in range(x2 - x1 + 1):
            drawPixel(x1+i, k*(x1+i)+d)


def drawTriangle(x1,y1,x2,y2,x3,y3):
    drawLine(x1,y1,x2,y2)
    drawLine(x1,y1,x3,y3)
    drawLine(x2,y2,x3,y3)

def drawRectangle(x1, y1, x2, y2):
    if (x1 is x2 ) or (y1 is y2):
        drawLine(x1, y1, x2, y2)
    else:
        drawLine(x1,y1,x1,y2)
        drawLine(x1,y1,x2,y1)
        drawLine(x1,y2,x2,y2)
        drawLine(x2,y1,x2,y2)


'''
def drawLine(x1,y1,x2,y2):
	for i in range((x2-x1)*100):
		drawPixel(x1+i/100,(y2-y1)/(x2-x1)*(x1+i/100)+(y1*x2-y2*x1)/(x2-x1))
'''

def test_drawline():
    #drawPixel(1, 3)
    #drawPixel(3, 9)
    #drawPixel(6,7)
    drawLine(1, 3, 6, 7)
    #drawLine(1,3,8,10)
    #drawLine(1.0,3.0,5,9)

def test_drawRecangle():
    drawRectangle(1,3,1,3)
    drawRectangle(7,3,9,3)
    drawRectangle(30,20,35,30)
    drawRectangle(40,50,80,90)

def test_drawTriangle():
    drawTriangle(20,40,20,55,40,40)
    #drawTriangle(2,5,3,6,8,12)

#test_drawline()
test_drawTriangle()
#testdrawRecangle()

c.display()



