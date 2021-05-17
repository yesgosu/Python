import turtle

def drow(t,r,f,n):
    for i in range(n):
            t.circle(r) # 원의수
            t.forward(f) # 반지름

t=turtle.Turtle()
drow(t,30,50,5) # 원의수,이동거리,반지름 설정
turtle.mainloop()