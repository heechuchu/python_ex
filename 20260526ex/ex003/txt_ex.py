# file = open('C:\\kgh\\phthon\\test.txt', 'w') # 파일을 '쓰기'모드로 open한다
# result = file.write('hello python!')                   # 쓰기(write)
# print(f'result: {result}')
# file.close()                                  # 파일닫기(외부자원해제)

# file = open('C:\\kgh\\phthon\\test.txt', 'r')
# readResult = file.read()
# print(f'readResult: {readResult}')
# print(f'readResult type: {type(readResult)}')

# readResult = int(readResult)
# readResult += 1
# print(f'readResult: {readResult}')
# file.close()


# file = open('C:\\kgh\\phthon\\test.txt', 'a')
# file.write('\nhello')
# file.close()

with open('C:\\kgh\\phthon\\test.txt','a') as file:
    for n in range(10):
        file.write('\nhello')   # 위와 같은 코딩, 문법만 다름

# file = open('C:\\kgh\\phthon\\test.txt', 'a')
# file.write('\nhi')
# file.close()

# 예외 처리(보험)
# 모든 프로그램은 100% 완벽할수 없어용

print(10 + 20)
try:
    print(10 / 1)

except Exception as e:
    print(f'e: {e}')

else:
    print('에러가 발생하지 않으면 실행되는 코드')

finally:
    print('에러가 발생하든 안하든 무조건 실행되는 코드')

print(10 - 20)
print(10 * 20)

# 예외처리 기본문법
'''
try ~ Exception
'''


