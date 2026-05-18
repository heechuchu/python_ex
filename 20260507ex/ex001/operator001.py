# 나눗셈 연산자 ( / )
# print(10 / 2) # 5.0
# print(3.14 / 0.5) # 6.28

# num1 = 100
# num2 = 10
# print(f'num1 / num2 = {num1 / num2}')

# quiz) BMI 구하기
# 몸무게와 신장입력하면 BMI를 계산해주는 프로그램
# bmi =  kg / 신장의 제곱 m2

# weight = float(input('몸무게(kg): '))
# height = float(input('신장(m): '))
# bmi = weight / (height * height)
# print(f'BMI: {bmi}')

# print(f'BMI: {bmi:.2f}') # 소수점 2번째자리까지만 나옴

# 숫자 0을 어떤 수로 나누어도 결과는 항상 0이다.
# print(0 / 123)  # 0

# # 어떤 숫자를 0으로 나눌 수 없다. 에러
# print(10 / 0)

# print(f'BMI: {bmi}')

# 나머지만, 몫, 거듭제곱
# 나머지만 (%)
# print(10 % 2)
# print(10 % 3)

# quiz) 홀짝 게임하기
# 주먹 쥔 손을 상대방에게 내밀며 손 안에 동전 개수가 홀수인지
# 짝수인지 맞추는 게임.
# 손 안에 동전 개수를 입력하면 짝수는 0, 홀수는 1 출력하는 프로그램
# inputData = int(input('손 안에 동전 수를 입력하세요.'))
# result = inputData % 2
# print(result)

# 몫(//)구하기
# print(10 // 3) # 3
# print(6 // 2) # 3

# quiz) 빵을 나누어 줄 수 있는 학생 수 구하기
# 길동이는 97개 빵을 3개씩 친구들 나눠주려함
# 최대 몇명에게 나눠줄수있는지, 남는빵 개수 구하기
# bread = 97
# breadCnt = 3
# maxFriendCnt = bread // breadCnt
# print(f'빵을 나눠 줄수있는 학생 수:{maxFriendCnt}')
# restBreadCnt = bread % breadCnt
# print(f'남는 빵 개수: {restBreadCnt}')


# 거듭제곱 구하는방법 (**)곱하기 두번
# print(2**2) # 4
# print(2**3) # 8
# print(2**10) #1024


# quiz) 전염병 예상 감염자 수 구하기
# 하루 한사람 한명
# 확진자 한사람이 나올경우 30일이후 몇명 감염자 나오는지 계산
# man = 2
# date = 30
# total = man ** date
# print(f'{date}일 이후 예상 감염자 수:{total}')


