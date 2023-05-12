from turtle import *

color('white', 'black')
begin_fill()
bgcolor("black")
speed(0.1)
setx(0)
sety(0)

while True:
    forward(150)
    left(119)
    if abs(pos()) < 1:
        break
end_fill()

done()