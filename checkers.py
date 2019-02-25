from graphics import*
#window size
winX = 800
check = True
#color for red and black
red = 244
#create window
wind = GraphWin("checker", winX, winX)
wind.setCoords(0, 0, winX, winX)
#cords
ly = 100
size = 75
#create board
for j in range (8):
    lx = 100
    #change color of start square
    if j %2 == 0:
        red = 0
    else:
        red = 244
    #draw a row
    for i in range (8):
        rSqu = Polygon(Point(lx,ly), Point(lx,ly + size), Point(lx + size,ly + size), Point(lx + size,ly))
        rSqu.setFill(color_rgb(red,0,0))
        rSqu.draw(wind)
        lx += 75
        if red == 0:
            red = 122
        if red == 244:
            red = 0
        red *= 2
    #move up a row
    ly += size
