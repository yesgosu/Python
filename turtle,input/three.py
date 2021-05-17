def mul(a,c):
    return a*c
def div(a,c):
    return a/c
def rest(a,c):
    return a % c
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def min(a,b):
    return a//b
while True:
    a=input("a: ") # 첫번째 숫자 받기
    if a !='q':
        op = input("+,-,%,/,* :") # input함수를 사용하여 계산식을 받는다.
        b = input("b :") # 두번째 숫자받기
        if op == "+":
            res = add(int(a),int(b))
        elif op=="-":
            res = sub(int(a),int(b))
        elif op=="*":
            res = mul(int(a),int(b))
        elif op=="/":
            res = div(int(a),int(b))
        elif op=="//":
            res = min(int(a),int(b))
        else:
            print("input error") # 잘못칠시 인풋에러라고 뜬다.

        print("result: ",res) # 계산을 하고 난 숫자가 뜬다.
        print("=============")
    else:
        print("good bye")
        exit(0)