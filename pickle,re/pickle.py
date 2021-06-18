import pickle

def start():
    address_book = {}  # 공백 딕셔너리를 생성한다.

    try:
        with open("addressData.txt", "rb") as f:
            addressData = pickle.load(f)
            print("파일을 불러왔습니다", addressData)
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
            address_book.pop(name)
            print(f'{name} 님이 삭제 되었습니다')

        elif user == 3: # 검색
            key = input("검색할 이름 입력 : ")
            if address_book.get(key) is None:
                print("저장되지 않은 이름입니다.")
            else:
                info = address_book.get(key)
                print(key, "의 전화번호 :", info[0])
                print(key, "의 주소 :", info[1])
                print(key, "의 이메일 :",info[2])
        elif user == 4: # 출력
            for key in sorted(address_book):
                info = address_book.get(key)
                print(key, "의 전화번호 :", info[0], key, "의 주소 :", info[1],key , "의 이메일 :",info[2])
        else:  # 파일 저장
            with open("./addressData.txt", "wb") as f:
                pickle.dump(address_book, f)
                f.close()
                print("파일이 저장되었습니다!")
                break

def get_contact():
    name = input("이름 : ")
    number = input("전화번호 :")
    add = input("주소 : ")
    mail = input("이메일 :")
    return (name, number, add,mail)


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