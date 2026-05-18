# 논리 연산자
# 논리 연산자는 피연산자의 논리자료형(True/False)을 이용하는 연산자로
# and, or, not이 있다

# and 연산자
# and는 '그리고' 라는뜻으로
# 피연산자가 모두 True인 경우에만 결과가 True
# 피연산자가 하나라도 False이면 결과는 False
var1 = True
var2 = True
print(var1 and var2) # True

var1 = True
var2 = False
print(var1 and var2) # False

var1 = False
var2 = False   
print(var1 and var2)  # False
print(var1 & var2) # and를 &로도 사용가능



# or 연산자
# or은 '또는' 뜻, 피연산자 중 하나라도 True라면 결과값은 True

var1 = True
var2 = True   
print(var1 or var2)  # True

var1 = True
var2 = False   
print(var1 or var2)  # True

var1 = False
var2 = False   
print(var1 or var2)  # False
print(f'var1 | var2 : {var1 | var2}') # or은 |로도 가능 쉬프트+\

# not(부정) 연산자
# not은 부정, 피연산자 현재 상태를 부정
# 피연산자가 True면 결과로 False를 출력, False면 True를 출력 
var1 = True
print(not var1) # False
var1 = False
print(not var1) # True

# quiz) 
num1 = 10; num2 = 20; num3 = 30
result = (num1 < num3) and (num2 < num3)
print(f'result: {result}') # True

result = (num1 > num3) and (num2 < num3)
print(f'result: {result}') # False

result = (num1 > num3) and (num2 > num3)
print(f'result: {result}') # False

result = (num1 < num2) and (num2 < num3) and (num3 > num1)
print(f'result: {result}') # True

print('-----------------------')
print(5 or 6) # 5
print(5 | 6)   # 7


# and, or 연산시 주의사항!
# and 연산자는 모든 피연산자가 True인 경우에만 True로 출력하기때문에
# 첫번째 연산의 결과가 False면 더이상 연산을 실행하지않음

num1 = 10; num2 = 20
result = (num1 < 15) and (num2 > 15)
print(num1 < 15) and (num2 > 15) # True

num1 = 17; num2 = 20
result = (num1 < 15) and (num2 > 15)
print(num1 < 15) and (num2 > 15) # False


# or 연산자는 피연산자중 하나라도 True가 있다면 결과값은 True이기때문에
# True 피연산자를 만나게 되면 피연산자의 연산은 무시하고 무조건 True를 출력

num1 = 10
print(f'num1: {num1}')
# print(abc)

# print((num1 > 5) or abc)


# quiz)어린이용 범퍼카 탑승가능 판별
# 범퍼카 사용기준 : 신장 120cm이상 170cm 미만어린이
# 범퍼카를 탑승할수 있는지 여부를 알려주는 프로그램 만들기
# 탑승 가능: True 탑승 불가: False

height = int(input('어린이 신장 입력'))
result = (height >= 120) and (height < 170)
print(f'result: {result}')

# 조건식 == 삼항 연산자
num1 = 10  # 이항 연산자라고도 함
num1 = 10 - 6 # 이항 연산자
not True     # 단항 연산자


targetScore = 90
myScore = 95
# myScore가 targetScore 보다 크거나 같으면 합격 , 그렇지 않으면 불합격
result = '합격' if myScore >= targetScore else '불합격' # 삼항연산자
print(f'result ---------> {result}')
# stringresult = myScore >= targetScore? '합격' : '불합격' # 자바식


# quiz) 적자 / 흑자 판단하기
# 수입과 지출입력하면 흑자인지 적자인지 판단하는 프로그램만들기
# 수익 결과 알려주는 프로그램
incoming = int(input('수입: '))
outgoing = int(input('지출: '))
result = '흑자' if incoming > outgoing else '적자'
print(f"result: {result}")

# quiz) 조명 장치 on/off 프로그램 만들기
currentLight = 50
targetLight = 60
result = 'Turn on'if currentLight < targetLight else 'Turn off'
print(f"result: {result}")

