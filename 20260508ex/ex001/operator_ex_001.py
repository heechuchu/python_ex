# # data = int (input ('수심을 입력하세요.'))
# # temperature = 20 - (data // 10 * .7)
# # print(f'temperature: {temperature}')


# # 속도와 시간을 입력하면 자동차의 주행거리를 구하는 프로그램
# # 주행속도 : 50
# # 주행시간 : 2
# # 주행 이동거리 : 100
# # 주행속도 : 110
# # 주행 시간: 2
# # 주행 이동 거리 : 220
# # speed = input('주행 속도: ')
# # time = input('주행 시간: ')
# # distance = int(speed) * int(time)
# # print(f'주행 거리: {distance}')

# # quiz) a회사는 3대의 컴퓨터로 8시간 일하면 하루업무처리가능
# # 단축근무를 하게 되어 근무시간 줄은다면 몇대 컴퓨터가 필요한가?
# # 근무 시간을 입력하면 필요한 컴퓨터 수량을 파악하는 프로그램 만들기
# computer = 3
# time = 8

# time = int(input("근무시간을 입력하세요. ")) # 단축 근무시간
# computer = (3 * 8) // time
# addComputer = 1 if (3 * 8 % time) > 0 else 0
# totalComputer = computer + addComputer
# print(f"필요한 컴퓨터수 {totalComputer}")

# maskPrice = 340
# maskCnt = int(input("마스크 구매 개수"))
# totalPrice = maskPrice * maskCnt
# cash = int(input("지불 금액: "))
# change = cash - totalPrice
# print(f'거스름돈:{change}')

# # 13시 30분 25초를 초로 나타내는 프로그램으로 만드시오.
# print(f'second: {25 + (60 * 30) + (60 * 60 * 13)}')

# 학생이 국어, 영어, 수학 점수를 입력하면 총점과 평균 출력하는 프로그램
# kor = int(input('국어점수: '))
# eng = int(input('영어점수: '))
# mat = int(input('수학점수: '))
# totalScore = kor + eng + mat
# averageScore = totalScore / 3
# print(f'totalScore: {totalScore}')
# print(f'averageScore: {averageScore}')

# 밤 최저 기온 낮 최고 기온 입력하면 일교차를 출력하는 프로그램
# low = int(input("밤 최저 기온 입력: "))
# high = int(input("낮 최고 기온 입력: "))
# difference = high - low
# print(f"difference: {difference}")

# 사용자가 길이(cm)입력하면 inch로 환산하는 프로그램(단, 1cm는 0.39inch로한다)
cm = int(input("길이 입력: "))
inch = cm * 0.39
print(f"inch: ",(inch))