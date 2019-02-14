from graphics import*
winX = 800
winY = 800
xran = 8
lX = 0
lY = 0
rX = 100
rY = 100
wind = GraphWin("checker", winX, winY)
wind.setCoords(0, 0, 800, 800)
#redsquare
def square(lx,ly,rx,ry,red):
    rSqu = Polygon(Point(lx,ly), Point(lx,ry), Point(rx,ry), Point(rx,ly))
    rSqu.setFill(color_rgb(red,0,0))
    rSqu.draw(wind)
    
#blacksquare

bSqu = Polygon(Point(100,0), Point(100,100), Point(200,100), Point(200,0))

for i in range(xran):
    for i in range(xran):
        square(lX,lY,rX,rY,255)
        lX += 100
        rX += 100
        square(lX,lY,rX,rY,0)
        lX += 100
        rX += 100
    

