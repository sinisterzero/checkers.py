from graphics import*
#define square
def square(lx,ly,rx,ry,red):
    rSqu = Polygon(Point(lx,ly), Point(lx,ry), Point(rx,ry), Point(rx,ly))
    rSqu.setFill(color_rgb(red,0,0))
    rSqu.draw(wind)
#window size
winX = 800
winY = 800
#color for red and black 
acolor = 255
bcolor = 0
#create window
wind = GraphWin("checker", winX, winY)
wind.setCoords(0, 0, 800, 800)
#cords
lX = 0
lY = 0
rX = 100
rY = 100
#create board
for j in range(8):
    if j %2 == 0:
        acolor = 0
        bcolor = 255
    else:
        acolor = 255
        bcolor = 0
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

    

