goods = {
    '새우깡': 1200,
    '비비빅': 400,
    '초코파이': 500,
    '맛동산': 1500
}
totalPrice = 0

def shrimpCrackerPrice():
    global totalPrice
    print(f"새우깡 구매 금액: {goods['새우깡'] * shrimpCrackers}")
    totalPrice += goods['새우깡'] * shrimpCrackers

def bibibigPrice():
    global totalPrice
    print(f"비비빅 구매 금액: {goods['비비빅'] * bibibigs}")
    totalPrice += goods['비비빅'] * bibibigs

def chocopiePrice():
    global totalPrice
    print(f"초코파이 구매 금액: {goods['초코파이'] * chocopies}")
    totalPrice += goods['초코파이'] * chocopies
def matdongsanPrice():
    global totalPrice
    print(f"맛동산 구매 금액: {goods['맛동산'] * matdongsans}")
    totalPrice += goods['맛동산'] * matdongsans

shrimpCrackers = int(input('새우깡 구매 개수: '))
bibibigs = int(input('비비빅 구매 개수: '))
chocopies = int(input('초코파이 구매 개수: '))
matdongsans = int(input('맛동산 구매 개수: '))

print(f'새우깡 구매 개수: {shrimpCrackers}')
print(f'비비빅 구매 개수: {bibibigs}')
print(f'초코파이 구매 개수: {chocopies}')
print(f'맛동산 구매 개수: {matdongsans}')
print('='* 40)
shrimpCrackerPrice()
bibibigPrice()
chocopiePrice()
matdongsanPrice()
print('=' * 40)
print(f'총 구매 금액: {totalPrice}')
print('=' * 40)

''' 결과 
새우깡 구매 개수: 3
비비빅 구매 개수: 2
초코파이 구매 개수: 1
맛동산 구매 개수: 2
새우깡 구매 개수: 3
비비빅 구매 개수: 2
초코파이 구매 개수: 1
맛동산 구매 개수: 2
========================================
새우깡 구매 금액: 3600
비비빅 구매 금액: 800
초코파이 구매 금액: 500
맛동산 구매 금액: 3000
========================================
총 구매 금액: 7900
========================================
'''

# 카페 음료 재고 관리 프로그램

'''
아메리카노 판매 개수:
라떼 판매 개수:
딸기스무디 판매 개수:
레몬에이드 판매 개수:
현재재고 - 판매개수

americano()
latte()
smoothie()
ade()

아메리카노 남은 재고: 7
라떼 남은 재고: 5
딸기스무디 남은 재고: 3
레몬에이드 남은 재고: 8

총 판매 개수: 15
재고보다 많이 판매하면: 재고 부족!
재고가 0이면: 품절입니다!
'''

drinks = {
    '아메리카노': 10,
    '라떼': 7,
    '딸기스무디': 5,
    '레몬에이드': 8
}

soldCount = 0


def americano():
    global soldCount

    if americanos > drinks['아메리카노']:
        print('아메리카노 재고 부족!')
    else:
        drinks['아메리카노'] -= americanos
        soldCount += americanos

        print(f"아메리카노 남은 재고: {drinks['아메리카노']}")

        if drinks['아메리카노'] == 0:
            print('아메리카노 품절입니다!')


def latte():
    global soldCount

    if lattes > drinks['라떼']:
        print('라떼 재고 부족!')
    else:
        drinks['라떼'] -= lattes
        soldCount += lattes

        print(f"라떼 남은 재고: {drinks['라떼']}")

        if drinks['라떼'] == 0:
            print('라떼 품절입니다!')


def smoothie():
    global soldCount

    if smoothies > drinks['딸기스무디']:
        print('딸기스무디 재고 부족!')
    else:
        drinks['딸기스무디'] -= smoothies
        soldCount += smoothies

        print(f"딸기스무디 남은 재고: {drinks['딸기스무디']}")

        if drinks['딸기스무디'] == 0:
            print('딸기스무디 품절입니다!')


def ade():
    global soldCount

    if ades > drinks['레몬에이드']:
        print('레몬에이드 재고 부족!')
    else:
        drinks['레몬에이드'] -= ades
        soldCount += ades

        print(f"레몬에이드 남은 재고: {drinks['레몬에이드']}")

        if drinks['레몬에이드'] == 0:
            print('레몬에이드 품절입니다!')


americanos = int(input('아메리카노 판매 개수: '))
lattes = int(input('라떼 판매 개수: '))
smoothies = int(input('딸기스무디 판매 개수: '))
ades = int(input('레몬에이드 판매 개수: '))

print('=' * 40)

americano()
latte()
smoothie()
ade()

print('=' * 40)

print(f'총 판매 개수: {soldCount}')

print('=' * 40)