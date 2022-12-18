x = 80
r = 50
def setup():
    size(600,400)
def draw():
    background(100)
    global x,r
    ellipse(r,200,100,100)
    strokeWeight(15)
    point(x,200)
    point(r,200)
    line(r,230,x,230)
    x += 5
    r += 5
