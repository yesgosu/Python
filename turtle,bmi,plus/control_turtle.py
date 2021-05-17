import turtle # 터틀 임포트

t = turtle.Turtle() # t 는 터틀이다.

def turtlemoveleft(t,a,d): # 함수선언
    t.left(a)   # 방향
    t.forward(d)    # 거리
def turtlemoveright(t,c,d):
    t.right(c)  # 방향
    t.forward(d)    # 거리
def turtlemoveforward(t,d):
    t.forward(d)    # 거리
def turtlemoveback(t,b):
    t.back(b)   # 뒤로가기


while True:
    command = input("command :")    # 값을 입력받는다
    if command == "l":  # l이면 왼쪽 90도로 100만큼 이동한다.
        turtlemoveleft(t,90,100)
    if command == "r":  # r이면 오른쪽 90도로 100만큼 이동한다.
        turtlemoveright(t,90,100)
    if command == "w":  # w이면 100만큼 전진한다.
        turtlemoveforward(t,100)
    if command == "b": # b이면 100만큼 뒤로 후진한다.
        turtlemoveback(t,100)
    if command == "q":  # q이면 프로그램이 정지한다.
        break