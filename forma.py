from turtle import *
color('blue', 'black')
begin_fill()
while True:
    speed(0)
    forward(200)
    right(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
