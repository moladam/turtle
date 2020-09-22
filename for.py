import turtle             
wn = turtle.Screen()        
alex = turtle.Turtle() 
n=360
h=1
sz=360/n
for i in range(n):
    alex.forward(h)
    alex.left(sz) 
