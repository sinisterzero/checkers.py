from graphics import*
#window size
print("Input the size of the board. Recommend less than 100 and more than 10")
size = int(input())
swap = {0: 244, 244:0}
#color
red = 244
#create window
wind = GraphWin("checker", size*10, size*10)
wind.setCoords(0, 0, size*10, size*10)
#create board
for j in range (8): #move up a row
    #change color of start square
    red = swap[red]
    for i in range (8): #draw a row
        rSqu = Rectangle(Point(size*(i+1),size*(j+1)), Point(size*(i+2),size*(j+2)))
        rSqu.setFill(color_rgb(red,0,0))
        rSqu.draw(wind)
        #change color
        red = swap[red]
