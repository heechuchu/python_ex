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
