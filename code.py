from turtle import *
color('white', 'black')
begin_fill()
bgcolor("black")
speed(1)
setx(0)
sety(0)

while True:
    forward(250)
    left(91)
    if abs(pos()) < 1:
        break
end_fill()

done()