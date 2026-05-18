# CRUD
'''
C: Create 생성,추가
R: Read   조회
U: Update 수정
D: Delete 삭제
'''

'''
딕셔너리(dictionary): key와 value로 데이터관리
'''
# Create

student = {
    '학번': 12345678,
    '이름': '홍길동',
    '나이': 20,
    '성별': 'M',
    '연락처': '010-1234-5678',
}

print(f'student: {student}')
print(f'student type: {type(student)}')

# Read

sNo = student['학번']
print(f'sNo: {sNo}')

# Update

sName = student['이름']
print(f'sName: {sName}') # 홍길동

student['이름'] = '홍길자' # 홍길동 > 홍길자
sName = student['이름']  
print(f'sName: {sName}')  # 홍길자

# Delete
del student['연락처'] 
print(f'student: {student}')

# keys(), values(), items()

# keys() : 딕셔너리 자료형에서 키값들만 몽땅 뽑는다.
#          뽑은 키들은 리스트와 비슷한 데이터 타입이다.
keys = student.keys()
print(f'keys: {keys}')
print(f'keys type: {type(keys)}')

for key in keys: # dict_keys(['학번', '이름', '나이', '성별'])
    print(f'key: value = {key}: {student[key]}')

# values(): 딕셔너리에서 value 값들만 몽땅 뽑는다.
#           뽑은 value들은 리스트와 비슷한 데이터 타입이다.
values = student.values()
print(f'values: {values}')  # dict_values([12345678, '홍길자', 20, 'M'])
print(f'values type: {type(values)}') 

for value in values:
    print(f'value: {value}')

# items()
items = student.items() # key & value 얻을수있다
print(f'items: {items}') # items: dict_items([('학번', 12345678), ('이름', '홍길자'), ('나이', 20), ('성별', 'M')])

for item in items:
    print(f'item: {item}')
    print(f'item[0], item[1]: {item[0]},{item[1]}')

'''
item 튜플 ==> ('학번', 123456789) ==> item[0], item[1]
'''

# 더 쉽게 뽑기
for key, value in items:     # 구조분해할당 문법
    print(f'key: value = {key}: {value}')

'''
key, value = ('학번', 123456789)
'''

# 구조분해할당
a, b = (10, 20)
print(f'a {a}, b: {b}')

# c = (10, 20)
# a = c[0]
# b = c[1]
# print(f'a {a}, b: {b}')

# a = 10
# b = 20
# # swapping ===> a: 20, b: 10
# temp = a
# a = b     # a : 20
# b = temp  # b : 10

# a ,b = b, a

scores = [10, 20, 30, 40, 50, 60]
'''
a = 10
b = 20
c = 30, 40, 50, 60
'''

a, b, *c = scores
print(f'a: {a}')
print(f'b: {b}')
print(f'c: {c}')

# quiz) 다음은 스포츠 센터 회원 정보를 나타낸 표이다.
# 표를 보고 파이썬을 이용해 컨테이너 자료형으로 만드시오.

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

members = {
    '2019-052001': '박찬호+25+M+010-1234-5678+헬스,수영+0'
}
info = members['2019-052001']
print(f'info: {info}') #'박찬호+25+M+010-1234-5678+헬스,수영+0'
infos = info.split('+') 
print(f'infos: {infos}')