weight = float(input("무게(kg) : ")) # 몸무게 값을 받아온다.
print("예시) 키가 183 일경우 1.83으로 표기") # 키의 경우 m표시이므로 오인의 경우가많아 미리 알려준다.
height = float(input("키(m) : ")) # 키의 값을 받아온다.

bmi = weight / height ** 2 # bmi = 몸무게를 키의 제곱으로 나눈값
print("당신의 BMI는 ",bmi)
if bmi >= 20.0 and bmi < 25.0: # bmi가 20.0보다 크거나 같거나, 25보다 작을경우 정상이라고 출력된다.
    print("정상입니다")
elif bmi >= 25.0 and bmi < 30.0: # bmi가 2.50보다 크거나 같거나, 30보다 작을경우 과체중이라고 출력된다.
    print("과체중입니다")
elif bmi >= 30.0:   # bmi가 30보다 크거나 같을경우 비만이라고 출력된다.
    print("비만입니다")
# 아래의 코드는 책의 bmi기준이 아닌 세계보건기구 기준이다.
# if bmi <= 18.5:
#     print("저체중입니다.")
# elif bmi > 18.5 and bmi <= 24.99:
#     print("평균체중입니다")
# elif bmi > 25.0 and bmi <= 29.99:
#     print("과체중입니다")
# elif bmi > 30.0 and bmi <= 34.99:
#     print("비만입니다")
# elif bmi > 35.0 and bmi <= 39.99:
#     print("중증 비만입니다")
# elif bmi > 40.0:
#     print("고도비만입니다.")

