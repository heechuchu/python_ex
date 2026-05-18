# # 딕셔너리(dictionary)
# # 인덱스 대신 키(key)를 이용하여 아이템을 참조합니다.
# # 딕셔너리는 키(key)와 값(value)의 쌍으로 이루어져있다.

# # 딕셔너리 정의
# # 딕셔너리는 {} 대괄호를 씀

# {'박찬호', '박지성', '박세리', '이승엽'}
# ages = {'박찬호': 48, '박지성': 40}
# print(f'ages: {ages}')
# print(f'ages type: {type(ages)}')


# scores = {
#     'c/c++': 'A',
#     'Java': 'B+',
#     '네트워킹': 'C',
#     '보안': 'A+',
#     '해킹': 'F',
#     '시스템': 'C+'
# }
# print(f'scores: {scores}')

# # 마지막 내용: ★★★★★★★★★★★★★★★★★★★★★★★★★★★
# # 리스트 , 튜플, 딕셔너리
# listVar = [3, 3.14, 'hello']
# print(f'listVar: {listVar}')

# dictVar = {
#     '홍길동': 10,
#     '박찬호': '열살',
#     '박세리': 3.14,
# }
# print(f'dictVar: {dictVar}')

# listVar1 = [1, 2, 3]
# listVar2 = [1, 2, 3, listVar]

# print(f'listVar1: {listVar1}') # [1, 2, 3]
# print(f'listVar2: {listVar2}') # [1, 2, 3,[1, 2, 3]]

# print(listVar2[3][1])       # [1, 2, 3] => 2

# print(type(listVar2[3]))    # list
# print(type(listVar2[3][1])) # int

# ##########################################################
# dicts = {
#     'name': '박찬호',
#     'age': 20,
#     'addr': '대전 중구',
#     'hobby': ['축구', '농구', '배구']
# }

# print(f'dicts: {dicts}')
# '''
# {'name': '박찬호', 'age': 20, 'addr': '대전 중구', 'hobby': ['축구', '농구', '배구']}
# '''

# dicts['hobby'][1]  # ['축구', '농구', '배구']
# print(dicts['hobby'[1]])

# '''
# nums[][][][][][][][][][][][][]][][]
# '''


'''
딕셔너리 조회/삽입/수정/삭제
컴퓨터 프로그램에서 '조회/삽입/수정/삭제'를 CRUD라고합니다..
CRUD라는 용어는 개발자라면 반드시 알고 있어야합니다.
CRUD는 create, Read, Update, Delete를 말합니다.
데이터를 생성(Create),조회(Read),수정(Update), 삭제(Delete)
그렇다면 딕셔너리에서 CRUD는 딕셔너리 컨테이너 자료형에
데이터를 추가(Create),조회(Read),수정(Update), 삭제(Delete)
CRUD는 프로그래밍 뿐만 아니라 데이터베이스에서도 사용되는 용어
 '''


# 추가(Create)
dicContainer = {
    '이름': '홍길동',
    '나이': '25',
    '주소': '대전 중구',
    '취미': ['축구', '수영', '조깅'],
    '몸무게': 87.5
}
print(f'dicContainer: {dicContainer}')

dicContainer['연락처'] = '010-1234-5678'
print(f'dicContainer: {dicContainer}')



# 조회(Read)
print(f'이름: {dicContainer['이름']}')


# 수정(update)
dicContainer['몸무게'] = 50
print(f'몸무게: {dicContainer['몸무게']}')


# 삭제(Delete)
del dicContainer['몸무게']
print(f'dicContainer: {dicContainer}')


# 부가기능
# 아이템 개수 조회
print(f'아이템 개수: {len(dicContainer)}')

# 전체 키 & 벨류를 조회
# 전체 키(key)
dicKeys = dicContainer.keys()
print(f'dicKeys: {dicKeys}')  #['이름', '나이', '주소', '취미', '연락처'])

for key in dicKeys:
    print(f'{key} : {dicContainer[key]}')

# 전체 벨류
dicValues = dicContainer.values()
print(f'dicValues: {dicValues}') #['홍길동', '25', '대전 중구', ['축구', '수영', '조깅'], '010-1234-5678']

# 키와 벨류를 한번에 조회

for key, value in dicContainer.items():
    print(f'{key}: {value}')

# print(dicContainer.item())
# print(type(dicContainer.item()))

# 중간고사 성적 관리 프로그램 만들기
'''
아래 시나리오를 기반으로 딕셔너리를 이용해서 중간고사 성적 관리 프로그램을 만들어봅시다.
 -1 : 중간고사의 성적(C/C++은 A, Java는 B+, 모바일은 C, 보안은 A+, 해킹은 F, 시스템은 C+)을 저장하는 
      딕셔너리를 만든다.
 -2 : 'Java'와 '시스템' 과목의 성적을 조회한다.
 -3 : 추가로 2과목의 성적(파이썬은 A, OS는 A+)을 삽입한다.
 -4 : 'Java'와 '시스템'의 성적을 각각 'F'와 'A'로 수정한다.
 -5 : 전체 과목과 성적을 조회하여 최종 성적표를 출력한다.
'''

scores = {
    'C/C++': 'A',
    'Java': 'B+',
    '모바일': 'C',
    '보안': 'A+',
    '해킹': 'F',
    '시스템': 'C+'

}

# -2'Java'와 '시스템' 과목의 성적을 조회한다.
print(f'Java: {scores['Java']}')
print(f'시스템: {scores['시스템']}')

# -3 추가로 2과목의 성적(파이썬은 A, OS는 A+)을 삽입한다
scores['파이썬'] = 'A'
scores['OS'] = 'A+'
print(f'scores: {scores}')

# -4'Java'와 '시스템'의 성적을 각각 'F'와 'A'로 수정한다.
scores['Java'] = 'F'
scores['시스템'] = 'A'
print(f'scores: {scores}')

# -5 : 전체 과목과 성적을 조회하여 최종 성적표를 출력한다.

creditScores = {
    'A+': 4.5,
    'A': 4.0,
    'B+': 3.5,
    'B': 3.0,
    'C+': 2.5,
    'C': 2.0,
    'F': 0.0,
}
totalScore = 0
averageScore = 0

for key in scores.keys():
    print(f'{key}:\t{scores[key]}')

print(f'totalScore: {totalScore}')  # 23.0
averageScore = totalScore / 8
print(f'averageScore: {averageScore}') # 2.875
'''
C/C++:  A       4.0
Java:   F       0.0
모바일:  C       2.0
보안:    A+      4.5
해킹:    F       0
시스템:  A       4.0
파이썬:  A       4.0
OS:     A+      4.0
'''
