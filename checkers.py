from graphics import*
#define square
def square(lx,ly,rx,ry,red):
    rSqu = Polygon(Point(lx,ly), Point(lx,ry), Point(rx,ry), Point(rx,ly))
    rSqu.setFill(color_rgb(red,0,0))
    rSqu.draw(wind)
    
winX = 800
winY = 800
xran = 8
acolor = 255
bcolor = 0

wind = GraphWin("checker", winX, winY)
wind.setCoords(0, 0, 800, 800)

lX = 0
lY = 0
rX = 100
rY = 100

for j in range(xran):
    for i in range(4):
        square(lX,lY,rX,rY,acolor)
        lX += 100
        rX += 100
        square(lX,lY,rX,rY,bcolor)
        lX += 100
        rX += 100
    lY += 100
    rY += 100
    lX = 0
    rX = 100

    

