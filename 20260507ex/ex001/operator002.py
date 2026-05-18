# 할당(대입) 연산자
# 할당 연산자는 변수에 값을 대입하는데 사용하는 연산자= '대입연산자'

# 할당 연산자(=)
num = 5
# 5가 num으로 할당
# 복합대입 연산자(+=, -=, *=, /=, %=, //=, **==)
# num = num + 5
# num += 5

# num = num - 5
# num -= 5

# num = num * 5
# num *= 5

# num = num % 5 
# num %= 5


# quiz) 복리 계산기 만들기
# 500만원씩 5년만기 가입했을때 5년 후 받을 총 수령액 (이자율:연5%)

myMoney = 5000000
rate = 0.05

# 1년 후 총 금액
myMoney = myMoney + (myMoney * rate)
# 2년 후 총 금액
myMoney = myMoney + (myMoney * rate)
# 3년 후 총 금액
myMoney = myMoney + (myMoney * rate)
# 4년 후 총 금액
myMoney = myMoney + (myMoney * rate)
# 5년 후 총 금액
myMoney = myMoney + (myMoney * rate)

# print(f'5년 후 총 수령액:{int(myMoney):,}원')

