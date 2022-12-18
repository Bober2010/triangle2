x = 600
r = 560
c = 150
t = 80
e = 50
def setup():
    size(400,800)
def draw():
    background(100)
    global x,r,c,t,e
    push()
    fill(205, 133, 63)
    ellipse(e,750,100,100)
    pop()
    strokeWeight(15)
    point(t,760)
    point(e,760)
    line(e,790,t,790)
    push()
    fill(139, 69, 19)
    rect(180,x,50,10000)
    pop()
    push()
    fill(0, 128, 0)
    ellipse(200,r,c,c)
    pop()
    x -= 5
    r -= 5
    c += 5
    x = 80
    r = 50
    t += 5
    e += 5

    

    
