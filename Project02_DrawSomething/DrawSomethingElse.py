from turtle import *

def go_to(x, y):

up()

goto(x, y)

down()

def Line(x,y):#直线 x=旋转角度 y=长度

right(x)

forward(y)

def H_circle(a,r,v):#画圆,a=旋转角度 b=圆的半径 v=角度

left(a)

circle(r,v)

def main():

pensize(2)

setup(1000,800,0,0)

color("green","green")

go_to(-250,300)

Line(78,77.5) #左耳朵

H_circle(104, -299, 57.5) #头

Line(-100,77.5) #右耳朵

Line(146,172)

H_circle(0,-76,53)#右脸

H_circle(5,-256,116)#下巴

H_circle(-2,-76,54)#左脸

Line(0, 173)#左耳朵

go_to(-270,150)

H_circle(-50,-134,64.5)#上眼皮

H_circle(-80,-78,136)#下眼皮

go_to(70,150)

H_circle(78,134,64.5)#上眼皮

H_circle(80,78,136)#下眼皮

go_to(70,-200)

write("TURINGCAT", move=True, align="left", font=("华文中宋", 40, "normal"))

done()

main()