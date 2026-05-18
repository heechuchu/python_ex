# #숫자 5개를 리스트에 저장한 뒤 가장 큰 숫자 출력하기

# # [3, 7, 1, 9, 5]

# # 9 

# numbers = [3, 7, 1, 9, 5]
# maxNum = 0
# for num in maxNum:
#     if num > maxNum:     # maxNum:0 num:3 > maxNum = 3
#         maxNum = num
# print(f'maxNum: {maxNum}')


# # 사용자에게 숫자 입력받아서
# # 1부터 입력한 숫자까지 합계 출력하기 ( 5 )

# userInputNum = int(input('양수 입력'))
# total = 0
# for i in range(1, userInputNum+1):
#     tota += num
#     print(f'total: {total}')

# # 리스트에 있는 숫자 중 짝수만 출력하기
# # [1,2,3,4,5,6]
# nums = [1, 2, 3, 4, 5, 6]

# for i in nums:
#     if i % 2 == 0:
#         print(i)


# # 리스트 숫자를 오름차순 정렬하기
# # [5,1,7,3]
# numbers = [5,1,7,3]
# numbers.sort()
# print(f'numbers:{numbers}')

# # 리스트 숫자를 내림차순 정렬하기
# # [5,1,7,3]
# numbers = [5,1,7,3]
# numbers.sort(reverse=True)
# print(f'numbers:{numbers}')

# # 리스트 안 숫자의 평균 구하기 [10,20,30]
# nums = [10, 20, 30]
# total = 0
# avg = 0
# for num in nums:
#     total += num

# avg = total / len(nums)
# print(f'total: {total}')
# print(f'avg: {avg}')


# # 리스트에서 가장 작은 숫자 찾기
# # (min() 사용 금지)
# numbers = [3, 7, 1, 9, 5]
# minNum = nums[0]   # 3
# for num in nums:
#     if num < minNum:
#         minNum = num
# print(f'minNum: {minNum}') # 1



# # 1부터 100까지 숫자 중
# # 3의 배수와 5의 배수 출력하기
# for num in range(1,101):
#     if num % 3 == 0:
#         print(f'{num}은 3의 배수')


#     if num % 5 == 0:
#         print(f'{num}은 5의 배수')
  

# # 사용자가 입력한 숫자를 리스트에 저장하다가
# # 0 입력하면 종료 후 리스트 출력하기
# # 입력: 3 ,입력: 7, 입력: 2 ,입력: 0

# # numbers = [3, 7, 2, 0]

# nums = []

# while True:
#     userInputNum = int(input('정수 입력: '))
#     if userInputNum == 0:
#         break

#     nums.append(userInputNum)
# print(f'nums: {nums}')

#######################################################
# -PC방 자리 관리 프로그램 

# 너는 PC방 사장이다.
# 손님이 자리에 앉으면 "사용중" 으로 바뀌고, 비어있으면 예약할 수 있다.

# seats = {
#     1: "빈자리",
#     2: "사용중",
#     3: "빈자리",
#     4: "사용중",
#     5: "빈자리"
# }
# 프로그램 요구사항
# 1.현재 자리 상태를 전부 출력하기
seats = {
    1: "빈자리",
    2: "사용중",
    3: "빈자리",
    4: "사용중",
    5: "빈자리"
}
print(f'seats: {seats}')

# 2. 사용자에게 원하는 자리 번호 입력받기

# 3.예약할 자리 번호 :

# 4.빈자리라면 "예약 완료" 출력 해당 자리 상태를 "사용중" 으로 변경 이미 사용중이라면 이미 사용중인 자리입니다 출력

# 5.예약 후 전체 자리 상태 다시 출력하기

# - 배달 주문 통계 프로그램 
# 배달 앱에서 하루 주문 데이터를 분석하려고 한다.
# 주어진 주문 목록
# orders = [
#     "치킨",
#     "피자",
#     "치킨",
#     "햄버거",
#     "피자",
#     "치킨"
# ]
# 프로그램 요구사

# 1. 각 음식이 몇 번 주문됐는지 딕셔너리에 저장하기
# 2. 가장 많이 주문된 음식 찾기
# 3. 총 주문 개수 출력하기
# 4. 사용자가 음식 이름 입력하면
# 몇 번 주문됐는지 출력하기

# -시험 결과 분석 프로그램 
# 학원에서 시험 결과를 분석하려고 한다.
# 주어진 데이터
# scores = {
#     "민수": 88,
#     "지훈": 72,
#     "수아": 95,
#     "유진": 64,
#     "서연": 100
# }
# 프로그램 요구사항
# 1.전체 학생 점수 출력하기
# 2.평균 점수 계산하기
# 3.최고 점수 학생 찾기
# 4.60점 이상은 합격, 미만은 불합격 출력하기 
# 90점 이상 학생 수 출력하기
# 6.점수 높은 순으로 학생 출력 도전하기

scores: ['민수': 88, '지훈': 72, '수아': 95, '유진': 64, '서연': 100]

total = 0
topstudent = ""
topScrore = 0

for score in scores:
    if score < 60:
        socres += 1

        total += score
    
if scores > 0 or topScrore < 60:
    print(f'불합격입니다. ')
else:
    print(f'합격입니다.')