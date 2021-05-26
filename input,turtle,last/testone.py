import random
f = int(input("정수를 입력하세요:")) # input으로 정수의 값을 친다.
for i in range(1,f+1): # for문으로 입력받은 값에 1을 더한다.
    for k in range(1,i+1): # 이중for문으로 i값에 1을 더한다.
        print(k,end=" ") # 이중for문으로 나온 k의 값을 출력한다.
    print()