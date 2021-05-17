def check_even_odd(number): 
    if(number % 2==0): # 2로 나눠서 나머지가 0일때 
        return "짝수입니다" # 짝수이다
    else:                   # 그렇지않으면
        return "홀수입니다"  # 홀수이다.

while True:
    number = int(input("숫자를 입력하세요: "))  # 값을 입력받는다
    if (number == 0000):    # 0000일때 break를 사용하여 프로그램 종료
        name = "시스템종료"
        exe = f'{name}' # print문의 f-string사용
        print(exe)
        break
    else:
        nve = check_even_odd(number)
        eve = f'{nve}'
        print(eve)
