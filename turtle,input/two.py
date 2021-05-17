import turtle
import random #랜덤 함수 사용

def drow(t,r,f,n): # 함수 정리
    mycolor=["blue","green","red"] # 색상을 정해줌
    if r == 'q':
        turtle.bye() # q를 누르면 프로그램이 종료된다.
        exit(0)
    else:
        for i in range(int(n)): # if문을 사용하여 원의수를 입력받는다.
            t.circle(int(r))
            t.forward(int(f))
            t.color(mycolor[random.randint(0,2)]) # 랜덤을 사용하여 블루,그린,레드중 랜덤으로 색상이 나온다
    turtle.mainloop()

r = input("반지름 입력")
f = input("이동거리 입력")
n = input("원의 수 입력")
t = turtle.Turtle()

drow(t,r,f,n)