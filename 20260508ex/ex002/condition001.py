# 조건문(if문)
# if 조건식:
#    4칸띄어쓰기 후 실행문 작성
# ex) if 키워드 조건식 콜론
#     if num  > 10 :
#    print('num은 10보다 크다.') --실행문

# num = 5
# if num > 10:
#     print('num은 10보다 크다.')
#     print('num은 10보다 크다.-----')
# print('num은 10보다 크다+++++')

# if 키워드: 조건문을 선언하기 위한 키워드로 '만약 ~라면'의 뜻
# 조건식: 특정 조건을 기술함. 조건식 결과에 따라 실행문의 실행여부가 결정
# 콜론(:): 코드 블록의 시작을 나타내며 콜론 이후부터가 실행될 문장이다
# 실행문: 조건식의 결과가 True인 경우 실행하는 명령문.
#        조건식이 False면 실행문은 실행되지않음.

# 사용자가 입력한 정수가 10보다크면 실행문을 출력하는 프로그램
# num = int(input('please input integer number'))

# if num > 10:
#     print(f'{num}은 10보다 크다.')

# if num == 10:
#     print(f'{num}은 10과 같다.')

# if num < 10:
#     print(f'{num}은 10보다 작다.')


# quiz) 속도위반 경고하기
# 제한속도가 50km/h인 도로에서 속도위반하는 자동차에 경고하는 프로그램

# limitSpeed = 50
# carSpeed = int(input("자동차 속도입력: "))

# if carSpeed > 50:
#     print(f'속도위반')

# if carSpeed <= 50:
#     print(f"정상속도")

# carSpeed = 40
# if carSpeed <= 50: print(f'정상속도') # 코드 간략화

# num = 5
# if num > 0:
#     print('num은 0보다 크다.')
#     print('num은 0보다 작다.')
# pass 

# if(만약) ~ else(그렇지않으면~) -> 양자 택일

# myScore = 70
# if myScore >= 90:
#     print('용돈획득')
# else:
#     print('빠따')

# if ~ elif -> 다중선택
# ex) 점수가 90점 이상이면 'A' 출력
#     점수가 80점이상 90점 미만이면 'B' 출력
#     점수가 70점이상 80점 미만이면 'C' 출력
#     점수가 60점이상 70점 미만이면 'D' 출력
# myScore = int(input('점수입력: '))
# if myScore >= 90:
#     print('A')
# elif myScore >= 80:
#     print('B')
# elif myScore >= 70:
#     print('C')
# elif myScore >= 60:
#     print('D') 
# else:
#     print('F')

# ex ) elif (myScore >- 80) and (myScore < 90)

# quiz) 자동 주문 시스템 만들기
# 다국어를 지원하는 식당에서 사용할 자동주문 시스템
# 1번 한국어 2번 영어 3번 중국어
# 그외 번호는 영어로 주문을 받는 프로그램
# 1. 대한민국 2. USA 3.中國 
# 1. 주문 하시겠습니까? 2. would you like to order? 3.您要点单吗？
# print("1.대한민국")
# print("2.USA")
# print("3.中國")
# lang = input("언어를 선택하세요.")


# if lang == "1":
#     print("주문하시겠습니까?")

# elif lang == "2":
#     print("would you like to order?")

# elif lang == "3":
#     print("您要点单吗？")

# else:
#     print("would you like to order?")



# selectedNumber = int(input('1. 대한민국 2. USA 3.中國'))
# if selectedNumber == 1:
#     print('주문하시겠습니까?')
# elif selectedNumber == 2:
#     print('would you like to order?')
# elif selectedNumber == 3:
#     print('您要点单吗？')
# else:
#     print("would you like to order?")

# KOREA_NUMBER = 1
# USA_NUMBER = 2
# CHINA_NUMBER = 3

# selectedNumber = int(input('1. 대한민국 2. USA 3.中國'))
# if selectedNumber == KOREA_NUMBER:
#     print('주문하시겠습니까?')
# elif selectedNumber == USA_NUMBER:
#     print('would you like to order?')
# elif selectedNumber == CHINA_NUMBER:
#     print('您要点单吗？')
# else:
#     print("would you like to order?")

# quiz) 국가재난지원금 수령액 조회하기
# 가구 인원수에 따른 국가재난지원금 수령액을 안내하는 프로그램
# 표를 참고하여 프로그램 만들기
# 1인가구: 400,000원 / 2인가구: 600,000원 / 3인가구: 800,000원 / 4인이상: 100만

# people = int(input("가구 인원수"))

# if people ==  1:
#     print('400,000원')
# elif people == 2:
#     print('600,000원')
# elif people == 3:
#     print('800,000원')
# else:
#     print("1,000,000원")


# quiz ) if ~ elif 문을 이용해서 만드시오
# BMI 지수입력
# BMI 지수 90이하 '저체중'
# BMI 지수 90초과 ~ 110이하 ' 정상체중'
# BMI 지수 110초과 ~ 120이하 '과체중'
# BMI 지수 120초과 ~ 140이하 '비만'
# BMI 지수 140초과 '고도비만'

# BMI = int(input('BMI지수입력: '))

# if BMI <= 90:
#      print('저체중')
# elif BMI <= 110:
#      print('정상체중')
# elif BMI <= 120:
#      print('과체중')
# elif BMI <= 140:
#      print('비만') 
# else:
#      print('고도비만')


# 중첩 조건문
# 조건문(실행문)내에 또 다른 조건문을 쓸 수있다. 이를 중첩 조건문이라함.
# 사용자가 입력한 정수에서 양수(0도 포함)인지를 판단하고 양수라면 홀/짝 구분

# myInteger = int(input('정수 입력: '))
# if myInteger >= 0:
#     print('양수')
#     if myInteger % 2 == 0:
#         print('짝수')
#     else:
#         print('홀수')
# else:
#     print('음수')

# quiz ) 짝수/홀수 판별하는 프로그램
# num = int(input('사용자야 양의 정수 입력해줘'))
# if num > 0:
#     if num % 2 == 0:
#         print('짝수')
#     else:
#         print('홀수')

# else:
#     print('입력한 정수는 0 또는 음수입니다.')


# quiz ) 년도 끝자리(endBirthyear)와 나이(Age)를 입력하면
# 다음 요구사항에 맞춰 마스크 구매 가능한 요일을 출력하는 프로그램
# 공적마스크 판매 관련 , 년도 끝자리 이용한 5부제
# 1,6 -> 월
# 2,7 -> 화
# 3,8 -> 수
# 4,9 -> 목
# 5,0 -> 금
# 만 65세이상은 언제든 구매가능

# endBirthyear = int(input('출생년도 끝자리 입력: '))
# age = int(input('나이 입력'))

# if age < 65:
#     if endBirthyear == 1 or endBirthyear == 6:
#         print('월요일 구매가능')
#     elif endBirthyear == 2 or endBirthyear == 7:
#         print('화요일 구매가능')
#     elif endBirthyear == 3 or endBirthyear == 8:
#         print('수요일 구매가능')
#     elif endBirthyear == 4 or endBirthyear == 9:
#         print('목요일 구매가능')
#     elif endBirthyear == 5 or endBirthyear == 0:
#         print('금요일 구매가능')
# else:
#     print('언제나 구매 가능')


# 날짜 관련 모듈
# datetime

# from datetime import datetime

#  현재 일(day) 구하기
# print(datetime. today().day)
# from datetime import datetime

# from datetime import datetime
# dayNum = datetime.today().day

# carNum = int(input('차량 4자리 번호입력'))

# print(f'오늘날짜: {dayNum} 일')

# if dayNum % 2 == 0:
#     print('오늘 입차: 번호가 짝수인 차량')

# else: 
#     print('오늘 입차: 번호가 홀수인 차량')

# if dayNum % 2 == carNum % 2:
#     print('귀하의 차량은 입차 가능합니다.')
# else:
#     print('귀하의 차량은 입차 불가합니다.')


# 생존율 출력 프로그램만들기
# 시간 60초 120초 180초 240초 300초 300초초과
# 생존율 85% 76% 66%    57%   47%  25%미만
# 최초장비를 사용하기까지 걸린 시간(초)입력: 70
# 생존율 76%

# time = int(input('최초 장비 사용하기까지 걸린시간(초) 입력: '))

# if time <= 60:
#     print("생존율 85%")
# elif time <= 120:
#     print("생존율 76%")
# elif time <= 180:
#     print("생존율 66%")
# elif time <= 240:
#     print("생존율 57%")
# elif time <= 300:
#     print("생존율 47%")
# else:
#     print("생존율 25미만%")


# 전기요금 계산기
# 사용량(kwh): 200이하 / 201~400이하 / 400초과
#    단가(원): 99.3   /  187.9     / 280.6
# 기본요금(원): 910    /  1600     /  7300
# price = 0
# basic = 0 

# kwh = int(input('전기 사용량을 입력하세요.'))


# if kwh <= 200:
#     price = 99.3
#     basic = 910
# elif kwh <= 400:
#     price = 187.9
#     basic = 1600
# else:
#     price = 280.6
#     basic = 7300

# total = ((kwh * price) + basic)

# print(f'사용량에 따른 요금: {total}')


# testScore = int(input('시험점수입력: '))
# result = 'success' if testScore >= 85 else 'fail'
# print(f'result:{result}')


# testScore = int(input('시험 점수 입력: '))
# if testScore >= 85:
#     print('success')
# else:
#     print('fail')

# import random       # 난수 발생 모듈

# ranNum = random.randint(1, 3)    # 1부터 3까지의 정수중에서 하나는 발생한다.

# myNum = int(input('1.가위  2.바위  3.보 를 선택하세요. '))

# if ranNum == 1 and myNum == 1:
#     print('무승부')

# elif ranNum == 1 and myNum == 2:
#     print('사용자 승')

# elif ranNum == 1 and myNum == 3:
#     print('컴퓨터 승')

# elif ranNum == 2 and myNum == 1:
#     print('컴퓨터 승')

# elif ranNum == 2 and myNum == 2:
#     print('무승부')

# elif ranNum == 2 and myNum == 3:
#     print('사용자 승')

# elif ranNum == 3 and myNum == 1:
#     print('사용자 승')

# elif ranNum == 3 and myNum == 2:
#     print('컴퓨터 승')

# elif ranNum == 3 and myNum == 3:
#     print('무승부')

# # 이렇게도 할수있음.
# elif (ranNum == 1 and myNum ==2) or (ranNum == 2 and myNum ==3) or (ranNum == 3 and myNum ==2):
#     print('사용자 승')


# quiz) 사용자가 입력한 문자메세지 길이에 따라 sms 또는 mms의 발송을
# 결정하는 프로그램을 완성하시오.
# (단, 메세지 길이가 50이하면 sms발송,50을 초과하면 mms를 발송)

# str = 'hello'  # hello
# print(f'str: {str}')
# print(f'str length: {len(str)}')  # 5
# str\'s => 출력하면 str's
# # usemsg = input('메세지를 입력하세요')
# # msgLen = len(usemsg)

# if msgLen <= 50:
#     print('sms발송')
# else:
#     print('mms발송')