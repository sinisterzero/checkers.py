from graphics import*
#window size
winX = 800
winY = 800
check = True
#color for red and black
red = 244
#create window
wind = GraphWin("checker", winX, winY)
wind.setCoords(0, 0, 800, 800)
#cords
ly = 100
ry = 175
#define square
for j in range (8):
    lx = 100
    rx = 175
    if j %2 == 0:
        red = 0
    else:
        red = 244
    for i in range (8):
        rSqu = Polygon(Point(lx,ly), Point(lx,ry), Point(rx,ry), Point(rx,ly))
        rSqu.setFill(color_rgb(red,0,0))
        rSqu.draw(wind)
        lx += 75
        rx += 75
        if red == 0:
            red = 122
        if red == 244:
            red = 0
        red *= 2
    ly += 75
    ry += 75
