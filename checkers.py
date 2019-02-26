from graphics import*

#window size
print("input the size of the board")
winX = int(input())
#color for red and black
red = 244
#create window
wind = GraphWin("checker", winX, winX)
wind.setCoords(0, 0, winX, winX)
#cords
ly = winX/10
size = winX/10
#create board
for j in range (8):
    lx = winX/10
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
        lx += winX/10
        if red == 0:
            red = 122
        if red == 244:
            red = 0
        red *= 2
    #move up a row
    ly += size
