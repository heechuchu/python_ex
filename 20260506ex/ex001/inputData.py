# 데이터 입력(input data)
# input()

'''
print('데이터를 입력하세요.')
inputData = input()
print(inputData)
'''

'''
print('정수를 입력하세요.')
inputInteger = input() 
print(inputInteger) 
print(type(inputInteger))
'''


'''
print('실수 입력하세요.') # 3.14
inputFloat = input()   # 3.14
print(inputFloat)      # str
print(type(inputFloat))
'''
'''
print('논리형 데이터 입력하세요.', end='') # 논리형 데이터 입력하세요. (자동개행)
inputBoolean = input()    # True
print(inputBoolean)       # True
print(type(inputBoolean)) # str
'''


# inputBoolean = input('논리형 데이터 입력하세요.\n')
# print(inputBoolean)       # True
# print(type(inputBoolean)) # str

#userInputData = input('사용자야 정수입력해라')  # 10
#print(userInputData)                         # 10
#print(type(userInputData))                   # str
#userInputData = int(userInputData)                           # str - - > int
#print(type(userInputData))         # int


# str -> boolean
# userInputData = input('True or False 입력하세요.')
# print(userInputData)                 # True
# print(type(userInputData))           # str
# userInputData = bool(userInputData) 
# print(type(userInputData))           # boolean

# str - > float
# userInputData = input('실수 입력하세요.')
# print(userInputData)
# print(type(userInputData))   # str
# userInputData = float(userInputData) 
# print(type(userInputData)) # float

# userInputData = 'True'
# userInputData = bool(userInputData)  
# print(type(userInputData))

# x = 3      # int  3
# y = float(x) # int -> float
# print(y) # 3.0

x = 3.141592
y = int(x) 
print(y) # 3
print(float(y)) # 3.0