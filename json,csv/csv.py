import csv
def start():
   address_book = {}  # 공백 딕셔너리를 생성한다.
   try:
       with open("./friendData.csv", "r") as f:
           data = csv.reader(f, delimiter=',')
           for line in data:
               for i in range(3):
                   line[i]=csv.sub('\n','',line[i])
               address_book[line[0]]={line[1],line[2]}
           print("파일을 불러왔습니다", address_book)
   except FileNotFoundError as e:
       print('파일이 존재하지 않습니다..', e)
   while True:
       user = display_menu()
       if user == 1:
           name, number, add = get_contact()
           info = [number, add]
           print('info', info)
           address_book[name] = info
       elif user == 2:  # 삭제
           name = input("삭제할 이름 입력 : ")
           if name not in address_book: #딕셔너리에 해당 이름이 없으면
               print("저장되지 않은 이름입니다.")
           else:
               del address_book[name]
               print(f'{name} 님이 삭제 되었습니다')
       elif user == 3: # 검색
           key = input("검색할 이름 입력 : ")
           if key not in address_book: #딕셔너리에 해당 키가 없으면
               print("저장되지 않은 이름입니다.")
           else:# 딕셔너리는 순서가 없으므로 각 값이 숫자로 시작하면 전화번호로 판단
               info=address_book[key]
               for val in info: #값들을 탐색
                   if val[0].isdigit(): #값의 첫문자가 숫자이면
                       contact=val #전화번호로 저장
                   else:
                       addr=val #아니면 주소로 저장
               print(key, "의 전화번호 :", contact)
               print(key, "의 주소 :", addr)
       elif user == 4: # 출력
           for key in sorted(address_book):
               info=address_book[key]
               for val in info:  # 값들을 탐색
                   if val[0].isdigit():  # 값의 첫문자가 숫자이면
                       contact=val #전화번호로 저장
                   else:
                       addr=val #아니면 주소로 저장
               print(key, "의 전화번호 :", contact, key, "의 주소 :", addr)
       else:  # 파일 저장
           with open("./friendData.csv","w",newline='') as f:
               writer = csv.writer(f)
               for key in address_book:
                   info = address_book[key]
                   for val in info:  # 값들을 탐색
                       if val[0].isdigit():  # 값의 첫문자가 숫자이면
                           contact = val
                       else:
                           addr = val
                   writer.writerow([key,contact,addr])
           print("파일이 저장되었습니다!")
           break
def get_contact():
   name = input("이름 : ")
   number = input("전화번호 :")
   add = input("주소 : ")
   return (name, number, add)
# 메뉴를 화면에 출력한다.
def display_menu():
   print("1. 연락처 추가")
   print("2. 연락처 삭제")
   print("3. 연락처 검색")
   print("4. 연락처 출력")
   print("5. 종료")
   select = int(input("메뉴 항목을 선택하시오: "))
   return select
# __main__은 프로그램의 시작점
if __name__ == '__main__':
   start()