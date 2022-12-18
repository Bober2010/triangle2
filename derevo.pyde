x = 600
r = 560
c = 150
def setup():
    size(400,800)
def draw():
    background(100)
    global x,r,c,v,b
    fill(139, 69, 19)
    rect(180,x,50,10000)
    fill(0, 128, 0)
    ellipse(200,r,c,c)
    x -= 5
    r -= 5
    c += 5
