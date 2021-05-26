import random # 랜덤을 임포트 한다.

for i in range(1,10): # for문을 사용하여 1부터 9까지를 불러온다.
    for k in range(1,10): # 이중for문을 사용하여 1부터 9까지를 출력한다.
        print(k*i,end=" ") # print문을 사용하여 k와i값을 곱셈한후 출력한다.
    print()