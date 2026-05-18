flag = True

members = {}

while flag:
    selectedMenuNum = int(input('1.회원가입  2.프로그램 종료'))

    if selectedMenuNum == 1:
        id = input('아이디: ')
        pw = input('비밀번호: ')
        members[id] = pw

    elif selectedMenuNum ==2:
        flag = False

        for key in members.keys():
            print(f'ID: {key}, Pw:{members[key]}')

########################################################
# 다음 딕셔너리에서 '3학점'인 과목을 모두 '5학점'으로 변경
classes =  {
    'python':'5학점', 'C/C++':'5학점',
    'HTML5':'3학점', 'Java':'5학점',
    'Javascript':'3학점'
    }

for key in classes:
    if classes[key] == '3학점':
        classes[key] = '5학점'
print(classes)

####################################################
# 컨테이너 자료형 만들기
'''
# list로 해보기

members = {
    '2019-052001': ['박찬호', 25, '남자', '010-1234-5678', '헬스, 수영', 0],
    '2019-052004': ['박용택', 65, '남자', '010-9012-3456', '수영', 50],
    '2019-052003': ['박세리', 70, '여자', '010-7890-1234', '아쿠아로빅', 50]
}

# 전체 회원 정보 출력

for key in members:
    print(f'회원번호: {key}, 회원정보: {members[key]}')
print('-' * 30)
# 전체 회원 정보 출력을 하는데, 회원이름과 성별만 출력해보기

for key, value in members.items():
    print(f'회원번호: {key}, 회원정보(이름, 성별): {value[0]}, {value[2]}')

'''


members = {
    '2019-052001': {
        '이름': '박찬호',
        '나이': 25,
        '성별': 'M',
        '연락처': '010-1234-5678',
        '이용서비스': ['헬스','수영'],
        '할인율': 0
},

'2019-052001': {
        '이름': '박용택',
        '나이': 65,
        '성별': 'M',
        '연락처': '010-9012-3456',
        '이용서비스': ['수영'],
        '할인율': 50
},
'2019-052001': {
        '이름': '박세리',
        '나이': 75,
        '성별': 'W',
        '연락처': '010-7890-1234',
        '이용서비스': ['아쿠아로빅'],
        '할인율': 50
}
}

# 전체 회원 정보 출력

for key, value in members.items():
    print(f'회원번호: {key}, 회원정보(이름, 성별): {value['이름']}, {value['성별']}')


# 전체 회원을 출력하는데 회원의 이름, 성별, 이용서비스만 출력
for key, value in members.items():
    print(f'회원번호: {key}, 회원정보(이름, 성별): {value['이름']}, {value['성별']}, {value['이용서비스']},{len(value['이용서비스'])}')

'''
# 다음 내용에 맞춰 냉장고에 보관하고 있는 야채의 재고 관리 프로그램만들기
1.당근 10개가 새롭게 입고되었다.
2.건대추 100개가 새롭게 입고되었다.
3.대파 20개가 새롭게 입고되었다.
4.애호박 3개가 새롭게 입고되었다.
5.부추 1개가 새롭게 입고되었다.
6.당근 1개가 소비되었다.
7.건대추 10개가 소비되었다.
8.대파 1개가 소비되었다.
9.애호박 1개가 소비되었다.
10.부추 1개가 소비되었다.
11.야채별 재고를 출력해 보자.
'''

Vegetables ={}

Vegetables["당근"] = 10
Vegetables["건대추"] = 100
Vegetables["대파"] = 20
Vegetables["애호박"] = 3
Vegetables["부추"] = 1


Vegetables["당근"] -= 1
Vegetables["건대추"] -= 10
Vegetables["애호박"] -= 1
Vegetables["부추"] -= 1

for key in Vegetables:
    print(f'{key} :{Vegetables[key]} 개')

# print('fff') # fff
# str = "ggg"
# print(str) # ggg

# print(f'fff {str}') # fff ggg


'''
철수 점수 85점 저장
영희 점수 92점 저장
민수 점수 78점 저장
학생들의 점수를 모두 출력하기
전체 점수 합계 출력하기
전체 평균 출력하기
'''

students = {
    '철수': 85,
    '영희': 92,
    '민수': 78,
}

for key in students:
    print(f'{key}: {students[key]}점')

total = 0

for key in students.values():
    total += key
    

average = total / len(students)

print(f'총점: ', total)
print(f'평균: ', average)


'''
주문 메뉴를 저장할 빈 리스트 만들기
손님에게 주문 개수를 입력받기
반복문으로 메뉴 이름 입력받아서 리스트에 추가하기
각 메뉴의 가격을 딕셔너리에 저장하기
떡볶이 : 4000원
순대 : 5000원
튀김 : 3000원
어묵 : 2000원
손님이 주문한 메뉴와 가격 출력하기
총 주문 금액 출력하기
'''

# 메뉴 가격 딕셔너리
menu_price = {
    "떡볶이": 4000,
    "순대": 5000,
    "튀김": 3000,
    "어묵": 2000
}

# 주문 리스트
orders = []

# 주문 개수 입력
count = int(input("주문 개수 입력: "))

# 메뉴 입력
for i in range(count):
    menu = input("메뉴 입력: ")
    orders.append(menu)

# 출력
print()
print("주문 메뉴")

# 총 금액
total = 0

for menu in orders:
    print(f"{menu} : {menu_price[menu]}원")
    total += menu_price[menu]

print()
print(f"총 금액 : {total}원")

'''
:: 용돈 기입장 만들기
'''


from datetime import datetime

MENU_INCOME     = 1
MENU_EXPENSE    = 2
MENU_VIEW       = 3
EXIT            = 99

flag = True
DEV_MOD = True

bankAccount = []
currentMoney = 0

if DEV_MOD:
    txt =  '[2026-05-15 15:14:08] \t 100 \t\t aaaaa \t\t 100'
    bankAccount.append(txt)
    txt = '[2026-05-15 15:15:08] \t 200 \t\t bbbbb \t\t 300'
    bankAccount.append(txt)
    txt = '[2026-05-15 15:16:08] \t\t -50 \t ccccc \t\t 250'
    bankAccount.append(txt)

while flag:

    selectedMenuNum = int(input('1.수입:    2.지출:    3.조회:    99.시스템종료 -----> '))
    if selectedMenuNum == MENU_INCOME:
        incomeMoney = int(input('수입 금액: '))
        incomeDesc = input('수입 내용: ')
        currentMoney += incomeMoney

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        txt = f'[{now}] \t {incomeMoney} \t {incomeDesc} \t\t\t {currentMoney}'
        bankAccount.append(txt)

    elif selectedMenuNum == MENU_EXPENSE:
        expenseMoney = int(input('지출 금액: '))
        expenseDesc = input('지출 내용: ')
        currentMoney -= expenseMoney

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        txt = f'[{now}] \t\t\t -{expenseMoney} \t {expenseDesc} \t {currentMoney}'
        bankAccount.append(txt)

    elif selectedMenuNum == MENU_VIEW:
        print('-' * 63)
        print('날짜&시간 \t\t 입금 \t 출금 \t 내역 \t\t 잔액')
        print('-' * 63)
        for item in bankAccount:
            print(item)
        print('-' * 63)

    elif selectedMenuNum == EXIT:
        flag = False 

