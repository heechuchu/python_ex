# 반복문(for문 & while문)
# for문: ~ 하는 동안 / 횟수의 의한 반복
# ex) for + 변수명 + in + 반복되는 범위 + :(콜론)
#    실행구문
# range = 범위를 지정하는 함수
# iterable = 반복가능한 객체
# for ~ in 키워드
# 1 ~ 10까지의 정수를 출력 (10까지라고하면 1을 더 붙임)
# 1 ~ n까지의 정수 range(1, (n+1),1)
# for num in range(1, 11, 1):
#     print(f'{num} : hello')
# for num in range(11):
#     print(f'{num} 안녕하세요')

# 0부터 10까지 정수출력
# for num in range(0, 11, 1):
#     print(f'num: {num}')

# #range()간략화 : 단계가 1인 경우 끝단계 생략 가능 
# 단계가 생략되고 시작이 0이면 시작도 생략가능
# for num in range(0, 11):
#     print(f'num: {num}')

# # quiz) 2~8 사이의 짝수 출력하기
# for num in range(2 ,9, 2):
#     print(f'num: {num}')
# ##################################
# for num in range(1, 16):
#     if num <= 8:
#         if num % 2 == 0:
#             print(f'num: {num}')
# ###################################
# for num in range(1, 16):
#     if (num <= 8) and (num % 2 == 0):
#             print(f'num: {num}')





# quiz) 사용자가 입력한 횟수만큼 '메일 발송!' 문자열 출력하기

# num = int(input("숫자입력: "))

# for mail in range(num):
#     print('메일발송!')

# 1~10 사이 정수를 출력하되, 정수가 3의 배수이면 '3의배수' 출력

# for num in range(1, 11):
#     if num % 3 == 0:
#         print("3의 배수")
#     else:
#         print(num)


# # 사용자가 원하는 구구단을 입력하면 해당 구구단 출력하기

# userInputData = int(input("출력할 구구단 입력: "))
# for dd in range(1, 10):
#     print(f"{userInputData} * {dd} = {userInputData * dd}")


# quiz 1 ~ 10까지의 정수의 합 출력하기
# userInputInteger = int(input('정수입력: '))
# sum = 0
# for i in range(1, 11):
#     sum += i
#     print(f"1부터 {userInputInteger}까지의 합: ", sum)

# quiz) for문 이용해서 1~100까지 정수중 3과 7의 공배수와 최소공배수 출력
# num1 = 100

# minNum = 0

# for num in range(1, 101):
#     if num % 3 == 0 and num % 7 == 0:
#         print(f'3과 7의 공배수: {num}')
#         if minNum == 0: minNum = num

# print(f'3과 7의 최소공배수: {minNum}')

##############################################

# range() 함수 정리

# 문자열을 이용한 for문 (★★★★★★★★★★★)
# 이터러블에는 다음과 같이 문자열 이용할수있음
# for ch in 'Hello':
#  print(f'ch: {ch}') 

# quiz) 50보다 작은 7의 배수를 출력하는 프로그램
# for num in range(1, 51):
#     if num % 7 == 0:
#         print(f'num: {num}')




# while문: ~하는 동안 / 조건에 의한 반복
# num = 1
# while num < 5:
#     print(num)
#     num +=1
# ''''''
# num = 1

# while num <= 10:
#     print(f'num: {num}')
#     num += 1
# ''''''

# quiz) 1~30까지의 정수 중 홀수와 짝수 구분하여 출력
# num = 1         # 시작
# while num < 31: # 조건(끝)
    
#     if num % 2 == 0:
#         print(f'{num}은 짝수')
#     else:
#         print(f'{num}은 홀수')

#         num += 1    # 단계


# quiz) 구구단 전체(2 ~ 9단) 출력하기



# num1 = 2
# while num1 <= 10:
        

#   num2 = 1  
# while num2 < 10:
#    print(f"{num1} x {num2} = {num1 * num2}")
#    num2 += 1
   
#    num1 += 1

# num1 = 1
# while num1 < 10:
#   num2 = 2 
#   str = ''


# while num2 < 10:
#   str += f'{num2} x {num1} = {num2 * num1}\t'
#   num2 += 1

# print(str)
# num1 += 1

# quiz) while문과 if문을 이용해서 0 ~ 100까지 정수중
# 3과 8의 공배수와 최소공배수 출력하기

# num = 1    # 반복문의 시작(초기값)
# minNum = 0 # 최소공배수

# while num <= 100:
#   if num % 3 == 0 and num % 8 == 0:
#     print(f'3과 8의 공배수: {num}') # 공배수 출력
    
#     if minNum == 0:
#       minNum = num   # 24
#   num += 1

# print(f'최소공배수: {minNum}')

# 반복문 내 실행 제어(break, continue)
# continue = 반복문에 continue 키워드를 사용하면
# 이후 실행을 생략하고 다시 반복문의 처음으로 돌아감

for num in range(1, 11):
  if num % 2 == 0:
    continue
  print(f'num: {num}') # 홀수만 출력 

# break = 반복문에서 break 키워드를 만나면 실행 중단,반복문 빠져나옴


# quiz ) 1부터 10까지 정수를 더하되, 결과가 30이상 될때 정수찾는 프로그램

num = 1
sum = 0

while num < 11:
  sum += num
  if sum >= 30:
    print(f'num: {num}')
    break
  num += 1

# for ~ else 키워드
# for문에 else 키워드 사용시 else이하 구문은 for문 반복업무로 모두완료후 실행됨
# 1~5까지 정수출력, 반복문 끝나면 완료 메세지 출력
for num in range(1, 6):
  print(f'num: {num}')
else:
  print('완료')


# pass 키워드
for num in range(1, 10):
  pass

# quiz) 삼각형넓이구하기
# 가로와 세로길이 변화에 따른 삼각형 넓이
# 가로길이는 1부터 2의배수 증가
# 세로길이는 1부터 3의 배수증가
# 삼각형 넓이가 150보다 크면 프로그램종료

cnt = 1
maxArea = 150

while True:
  result = ((cnt * 2) * (cnt * 3)) / 2
  if result > 150: break
  print(f'삼각형넓이: {result}')
  cnt += 1