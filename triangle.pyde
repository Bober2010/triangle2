v = 150
r = 450
x = 150
def setup():
    size(600,600)
def draw():
    global x,r,v
    triangle(300,v,250,250,350,250)   
    triangle(200,350,x,450,250,450)   
    triangle(400,350,350,450,r,450)
    x -= 1
    r += 1 
    v -= 1 
