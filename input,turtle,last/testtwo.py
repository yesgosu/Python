import turtle # 터틀을 임포트 하였다.
import random # 랜덤을 임포트하였다.
t = turtle.Turtle() # T는 터틀이다.
for i in range(10): # 터틀의 원을 10번 실행하게 만들었다.
    x = random.randint(-200,200) # X의 값을 랜덤으로 좌표를 -200,200으로 설정해주었다.
    y = random.randint(-200,200) # Y의 값을 랜덤으로 좌표를 -200,200으로 설정해주었다.


    t.penup() # 펜을 그린다.
    t.goto(x,y) # x,y축을 랜덤으로 설정해주어서 좌표가 랜덤이다.
    r = random.randint(1,100) # r은 랜덤 반지름을 설정해주었다,1부터100까지
    t.pendown() # 펜을 놓는다.
    t.circle(r)
t.mainloop