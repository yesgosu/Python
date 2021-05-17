import random

i = 0       #반복을 위해 선언
score = 0   #스코어
while i<5:  #i가 5 미만일 때까지 반복
    x = random.randint(1,100) # 1부터 100까지의 랜덤값
    y = random.randint(1,100)
    answer = int(input("{0}+{1} =".format(x,y))) # x,y값을 format로 출력
    if answer == (x+y):
        score+=10
    i+=1    #i를 1 더해줌 0,1,2,3,4로 5번 반복하게됨
print("최종 점수 = {0}, 수행 회수 = {1}".format(score,i))
