# 클래스(객체를 만들기 위한 틀(설계도)) 문법
# 붕어빵클래스

class FishBread:   # 클래스 선언

    # 속성(attribute)
    def __init__(self, f, b):
        self.flour = f
        self.bean = b

    # 기능(function, method)
    def makeFishBread(self):
        print('붕어빵 제조')

# 붕어빵 클래스로부터 객체를 만들어봅시다(객체 생성)
myFishBread = FishBread('팥', '밀가루')
friendFishBread = FishBread('호박', '쌀')
hisFishBread = FishBread('꿀', '밀가루')

print(f'내 붕어빵의 속 내용물: {myFishBread.flour}') # 팥
print(f'내 붕어빵의 속 반죽: {myFishBread.bean}')   # 밀가루

print(f'친구 붕어빵의 속 내용물: {friendFishBread.flour}') # 호박
print(f'친구 붕어빵의 속 반죽: {friendFishBread.bean}')   # 쌀

print(f'그의 붕어빵의 속 내용물: {hisFishBread.flour}') # 꿀
print(f'그의 붕어빵의 속 반죽: {hisFishBread.bean}')   # 밀가루


# 계산기 클래스
class Calculator:
    # 속성
    def __init__(self, n1, n2):
        self.num1 = n1
        self.num2 = n2
    
    # 기능
    def add(self):
        print(f'add: {self.num1 + self.num2}')
    def sub(self):
        print(f'sub: {self.num1 - self.num2}')
    def mul(self):
        print(f'mul: {self.num1 * self.num2}')
    def div(self):
        print(f'div: {self.num1 / self.num2}')

mycalculator = Calculator(10, 20)
friendcalculator = Calculator(100, 200)

mycalculator.add()
mycalculator.sub()
mycalculator.mul()
mycalculator.div()

# 인간 클래스
class Human:
    #속성
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    #기능
    def walk(self):
        print('걷자!!')
    def run(self):
        print('달리자!!')

    def printMyInfo(self):
        print(f'나의 신장: {self.height}')
        print(f'나의 체중: {self.weight}')

human1 = Human(188, 87)
human2 = Human(165, 49)

human1.printMyInfo()
human2.printMyInfo()
