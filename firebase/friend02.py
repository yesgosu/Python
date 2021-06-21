from tkinter import *  # tinker 임포트
import pyrebase

firebaseConfig = { # 파이어베이스 연결
    "apiKey": "AIzaSyA1fE08wsj3YwWZUV5ybSxtmwFwQRWYiao",
    "authDomain": "friend-dc426.firebaseapp.com",
    "databaseURL": "https://friend-dc426-default-rtdb.firebaseio.com",
    "projectId": "friend-dc426",
    "storageBucket": "friend-dc426.appspot.com",
    "messagingSenderId": "78508764036",
    "appId": "1:78508764036:web:b6c62e81d00d961f1c8bd1",
    "measurementId": "G-QHQ73VMH3S"
  };
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

ar = {}  # 공백 딕셔너리 생성
def run(): #파이어베이스 디비연결
    all_users = db.child("AddressBook2").get()
    for users in all_users.each():
        print(users.val())
        print(users.key())
        ar[users.key()] = users.val()
def search() : # 검색
    e1.focus_set()
    print("검색")
    name = e1.get()
    if name == '':
        txt.insert(END, f'정보가 입력되지 않았습니다\n')
    elif name not in ar.keys():
        txt.insert(END, f'정보가 존재하지 않습니다\n')
    else:
        for key in (ar):
            if key == name:
                txt.insert(END, f'{key}의 정보를 검색 했습니다\n')
                txt.insert(END, f'{key}의 전화번호 : {ar[key][0]}\n')
                txt.insert(END, f'{key}의 주소 : {ar[key][1]}\n')
                txt.insert(END, f'{key}의 이메일 : {ar[key][2]}\n')
    e1.delete(0, END)


def add() :  # 추가
    e1.focus_set()

    name = e1.get()
    phone = e2.get()
    address = e3.get()
    email = e4.get()
    info = [phone,address,email]
    if name == '' or phone == '' or address == '' or email == '':
        txt.insert(END, f'입력 정보가 비어있습니다\n')
    else:
        print("추가")
        db.child("AddressBook2").child(name).set(info)
        txt.insert(END, f'{e1.get()}의 정보를 목록에 추가 했습니다\n')
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        run ()
def delete() : #삭제
    e1.focus_set()
    name = e1.get()
    if name == '':
        txt.insert(END, f'입력 정보가 비어있습니다\n')
    else:
        print("삭제")
        ar.pop(name)
        txt.insert(END, f'{e1.get()}의 정보를 목록에서 삭제 했습니다\n')
        e1.delete(0, END)
        db.child ( "AddressBook2" ).child ( name ).remove ()
        run ()

def output() : # 출력하기
    e1.focus_set()
    run ()
    print("출력")
    for key in sorted(ar):
        txt.insert(END, f'{key}의 전화번호 : {ar[key][0]}, 주소 : {ar[key][1]}\n , 이메일 : {ar[key][2]}\n')
    e1.delete(0, END)

def update(): # 수정
    e1.focus_set()
    all_users = db.child("AddressBook2").get()
    name = e1.get()
    phone = e2.get()
    address = e3.get()
    email = e4.get()
    if name=='' or phone=='' or address=='' or email=='':
        txt.insert(END, f'입력 정보가 비어있습니다\n')
    elif name not in all_users.val():
        txt.insert ( END, f'등록된 정보가 없습니다\n' )
    else:
        print("수정")
        db.child("AddressBook2").child(name).update({"0":phone})
        db.child("AddressBook2").child(name).update({"1": address})
        db.child("AddressBook2").child(name).update({"2": email})
        txt.insert(END, f'해당 유저의 정보가 수정되었습니다\n')
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()



def saveExit() : # 종료
    print("종료")
    txt.insert(END, "종료")
    exit()


window = Tk()
f = Frame(window, bg="yellow")

l1 = Label(window, text="이름")
l1.grid(row=0,column=0, pady=10)
l2 = Label(window, text="전화번호")
l2.grid(row=1,column=0, pady=10)
l3 = Label(window, text="주소")
l3.grid(row=2,column=0, pady=10)
l4 = Label(window, text="이메일")
l4.grid(row=3,column=0, pady=10)
e1 = Entry(window)
e1.grid(row=0,column=1)
e2 = Entry(window)
e2.grid(row=1,column=1)
e3 = Entry(window)
e3.grid(row=2,column=1)
e4 = Entry(window)
e4.grid(row=3,column=1)

f.grid(row=4,column=0, columnspan=2)

b1 = Button(f, text="검색", command=search, padx=10)
b1.grid(row=0,column=0)
b2 = Button(f, text="추가", command=add, padx=10)
b2.grid(row=0,column=1)
b3 = Button(f, text="삭제", command=delete, padx=10)
b3.grid(row=0,column=2)
b4 = Button(f, text="출력", command=output, padx=10)
b4.grid(row=0,column=3)
b5 = Button(f, text="수정", command=update, padx=10)
b5.grid(row=0,column=4)
b6 = Button(f, text="종료", command=saveExit, padx=10)
b6.grid(row=0,column=5)


txt = Listbox(window,width=34,height=20, bg="White")
txt.grid(row=5,column=0,columnspan=2, pady=10)

scrollbar = Scrollbar(window, orient='vertical')
scrollbar.grid(row=5, column=2, sticky=N+S)

txt.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=txt.yview)

window.mainloop()
run()