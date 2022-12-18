z = 90
x = 70
c = 110
b = 255
a = 0
p = 90
q = 80
def setup():
    size(600,400)
def draw():
    background(100)
    global z,x,c,b,a,p,q
    ellipse (z,200,150,150)
    push()
    frameRate(10)
    fill(random(a),random(b),random(c))
    ellipse (x,200,30,30)
    fill(random(c),random(b),random(a))
    ellipse (c,200,30,30)
    pop()
    push()
    strokeWeight(10)
    line(x,230,c,230)
    pop()
    ellipse(x,150,c,80)
    ellipse(x,130,p,90)
    z += 5
    x += 5
    c += 5
    b -= 0
    a -= 0
    p -= 5
