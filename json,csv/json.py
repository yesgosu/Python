import json

def start():
   address_book = {}  # 공백 딕셔너리를 생성한다.
   try:
       with open("./friendData.json", "r") as f:
           address_book=json.load(f)
           print(address_book)
   except FileNotFoundError as e:
       print('파일이 존재하지 않습니다..', e)
   while True:
       user = display_menu()
       if user == 1:
           name, number, add,email = get_contact()
           info = [number, add,email]
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
               print(key, "의 이메일 : ", email)
       elif user == 4: # 출력
           for key in sorted(address_book):
               info=address_book[key]
               for val in info:  # 값들을 탐색
                   if val[0].isdigit():  # 값의 첫문자가 숫자이면
                       contact=val #전화번호로 저장
                   else:
                       addr=val #아니면 주소로 저장
                       print(key, "의 전화번호 :", contact, key, "의 주소 :", addr, key , "의 이메일 : ",email)
       else:  # 파일 저장
           with open("./friendData.json","w",encoding='utf-8') as f:
               json.dump(address_book,f,ensure_ascii=False,indent=4)
           print("파일이 저장되었습니다!")
           f.close()
           break
def get_contact():
   name = input("이름 : ")
   number = input("전화번호 :")
   add = input("주소 : ")
   email = input("이메일 :")
   return (name, number, add,email)
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