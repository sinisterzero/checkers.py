from graphics import*
def drawSqu(x, color, window):
    rSqu = Rectangle(Point(x*(i+1),x*(j+1)), Point(x*(i+2),x*(j+2)))
    rSqu.setFill(color_rgb(color,0,0))
    rSqu.draw(window)
#window size
print("Input the size of the board. Recommend less than 100 and more than 10, no odd number")
size = int(input())
swap = {0: 244, 244:0} #swap color
#color
red = 244
#create window
wind = GraphWin("checker", size*10, size*10)
wind.setCoords(0, 0, size*10, size*10)
#create board
for j in range (8): #move up a row
    red = swap[red]#swap color for starting square
    for i in range (8): #draw a row
        drawSqu(size, red, wind)
        #change color
        red = swap[red]
