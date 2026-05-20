# 지역변수 vs 전역변수
# 지역변수는 함수 내부에서 선언된 변수로, 함수 내부에서만 사용가능
# 전역변수는 함수 외부에서 선언된 변수로, 함수 내/외부에서 사용가능

num = 10

def fun():
    # num = 20
    global num
    num + num + 1   # 데이터수정 num(전역변수) = 10 + 1 
    print(f'num: {num}') # 10, 전역변수

print(f'num: {num}')   # 10, 전역변수 5line 

fun()

'''
global 키워드는 함수 내에서 전역변수의 값을 
'수정'하고자할때 반드시 명시하자
'''

# quiz) 웹사이트의 누적방문 횟수 프로그램
# 방문여부를 입력받아 웹사이트의 누적방문횟수를 출력학기

flag = True
totalVisitor = 0

def countVisitor():
    global totalVisitor
    totalVisitor += 1

while flag:
    seletedMenuNum = int(input('1.웹사이트 방문   2.종료'))

    if seletedMenuNum == 1:
        countVisitor()
        print(f'누적 방문 수: {totalVisitor}')
    else:
        flag = False
        print(f'good bye')


# 매개변수 (매우중요함)
# 매개: 둘 사이에서 양편의 '관계를 맺어' 줌
# 함수를 사용하기 위해 먼저 함수를 정의하고 필요할 때 호출함.
# 이 때 함수를 정의하는 쪽을 함수 정의부(선언부), 
# 함수를 호출하는 쪽을 호출부라고 함

# 함수를 호출할 때 데이터를 넘겨줄 수 있다. 
# 이 데이터를 '인수'라고 함
# 함수 정의부는 인수를 받으면 '매개변수'라는 변수에 저장함
# 그리고 매개변수는 지역변수의 일종임.

def greet(name, age): # 홍길동,박찬호,박세리
    print(f'{name} 씨, 안녕하세요. 나이는 {age}입니다')

greet('홍길동',25)
greet('박찬호',20)
greet('박세리',30)


# 날씨를 출력해주는 프로그램

def forecastWether(temp, humi, rain):
    print('날씨 예보입니다.')
    print(f'최고 온도:  {temp}도')
    print(f'평균 습도: {humi}%')
    print(f'비 올 확률: {rain}%')

forecastWether(32, 67, 50)


# 인수의 개 수를 모르는 경우
# 우리 학급 학생들의 시험점수 총 합과 평균을 구하는 함수를 만들자!
# 학급 학생 수는 총 3명이다

# def printScoresForStudent(score1, score2, socre3):
#     totalScore = score1 + score2 + socre3
#     averageScore = totalScore / 3 # 평균값
#     print(f'총합: {totalScore}')
#     print(f'평균: {averageScore}')

def printScoresForStudent(*scores): # 가변인자 -> 튜플로 저장 
    
    print(f'scores type: {type(scores)}') # tuple
    print(f'scores length: {len(scores)}')
   
    totalScore = 0

    for score in scores:
        totalScore += score

    print(f'총합: {totalScore}')
    print(f'평균: {totalScore / len(scores)}')

printScoresForStudent(90, 80, 100)

'''
선생님이 몇명일지 모르는 점수를 입력한다
이때 학생 점수의 총합과 평균을 구하는 함수를 만들고
이를 이용하는 프로그램을 만들자
'''
flag = True
studentScores = []

def printScoresForStudent(scores):   # scores = [,,,,,]
    totalScore = 0
    for score in scores:
        totalScore += score
    
    average = totalScore / len(scores)
    print(f'총점: {totalScore}')
    print(f'평점: {totalScore / len(scores)}')

while flag:
    seletedMenuNum = int(input('1.학생점수입력 2.종료'))
    if seletedMenuNum == 1:
     score = int(input('학생 점수 입력: '))
     studentScores.append(score)
    else:
        flag = False

printScoresForStudent(studentScores)

# quiz) SMS와 MMS 구별하기
'''
문자를 보낼 때 100자 이하인 경우에는 단문 메시지(SMS)로 50원을 부과합니다.
그런데 100자를 넘어가면 장문 메시지(MMS)로 변경되면서 100원이 부과됩니다. 
단문과 장문을 구별해서 돈을 부과하는 프로그램을 만들어봅시다. 
'''
def sendUserMessage(str):
    strLength = len(str)
    print(f'사용자가 입력한 문자길이: {strLength}')

    if strLength <= 100:
        print(f'SMS 발송 완료')
        print('50원 부과')
    else:
        print(f'MMS 발송 완료')
        print('100원 부과')

inputData = input('문자 입력')


######################################################

# 인수와 매개변수의 순서가 일치하지않을 경우

# def printMemberInfo(name, email, major, grade):
#     print(f'name\t: {name}')
#     print(f'email\t: {email}')
#     print(f'major\t: {major}')
#     print(f'grade\t: {grade}')
#     print('----------------------------------')

# printMemberInfo('Hong Gil Dong', 'gildong@gamil.com', 'art', 1)
# printMemberInfo(email = 'gildong@gamil.com',
#                 name = 'Hong Gil Dong',
#                 major= 'art',
#                 grade = 1) # 좋지않은 방법.
'''
info = {
        'name': 'honggildong',
        'email': 'gildong@gmail.com',
        'major': 'art',
        'grade': 1,
    }
'''
# 이렇게하면 순서 뒤바껴도 상관없음 
def printMemberInfo(info):
    print(f'name: {info['name']}')
    print(f'email: {info['email']}')
    print(f'major: {info['major']}')
    print(f'grade: {info['grade']}')

printMemberInfo( {
        'name': 'honggildong',
        'email': 'gildong@gmail.com',
        'major': 'art',
        'grade': 1,
    }
)

# 매개변수의 기본값 설정 
# 직원 급여 지급 프로그램 만들기
def setSalary(name, pay = 200):
    print(f'{name}의 급여{pay}원 지급')

setSalary('박찬호', 400)
setSalary('박세리', 600)
setSalary('박용택')  # 매개변수기본값 = 200 (최소 월급)

# [].sort() # reverse = False
# [].sort(reverse=True)


# 데이터 반환 (return)
# 데이터 반환이란, 함수는 실행이 끝난 후에 결과물(값)을 호출부로 반환할수있음
# 이때 사용하는 키워드가 return

# 덧셈 연산 함수를 만들어 결과를 출력하는 프로그램

def printResult(value):
    print(f'result: {value}')

def addFuntion(n1, n2):
    sum = n1 + n2  # 30
    # print(f'결과값: {sum}')
    print(sum)
    return sum

result = addFuntion(10, 20)


#############################################
DEV_MOD = True # False하게되면 2가 안뽑힘 (return넣을시)

def fun1():
    print('11111111111')
    # return -> 선언과 함께 종결도 가능 
    if DEV_MOD == True:
        print('22222222222') # 개발단계에서 디버깅 용도로만 사용
    print('33333333333')

fun1()


# 별탑 만들기

def increaseStart():
    
    for n in range(1, 8):
        print('*' * n) # 아래것과 동일
        # if n == 5: 5와같다면종료
        #  break
#     print('*')
#     print('**')
#     print('***')
#     print('****')
#     print('*****')
#     print('******')
#     print('*******')
increaseStart()


# Toy 프로젝트 진행 
'''
처음 프로그램이 실행되면 다음과 같은 메뉴를 출력한다.
메뉴: 1. 회원가입 2. 로그인 3. 특정 회원 정보 출력 4.모든 회원정보출력 99.종료
사용자가 1. 회원가입하면 회원가입ID, 회원PW, email, 회원연락
정보를 입력받아 회원가입 진행 하기
2. 로그인을 하면 ID,PW 입력받아 로그인성공 또는 실패 출력
3. 특정회원을 선택하면 ID와 PW입력받아 일치하는 회원정보를 모두 출력
4. 가입되어있는 모든 회원 정보 출력
99.종료
- 특정회원의 ID, PW 인증되면 회원정보 수정하는 기능구현해보기
'''
members = []

while True:
    print('1. 회원가입')
    print('2. 로그인')
    print('3. 특정 회원정보')
    print('4. 모든 회원정보')
    print('99.종료')

    menu = int(input('선택: '))

    if menu == 1:
        memberId = (input('아이디 입력: '))
        memberPw = (input('비밀번호 입력: '))
        memberEm = (input('이메일아이디 입력: '))
        memberNum = (input('연락처 입력: '))
        
        member = {
            'id': memberId,
            'pw': memberPw,
            'email': memberEm,
            'phoneNum': memberNum
        }
        members.append(member)
        print(f'회원가입완료')

    elif menu == 2:
        loginId = input('ID입력: ')
        loginPw = input('PW입력: ')

    loginSuccess = False

    for member in members:

     if member['id'] == loginId and member['pw'] == loginPw:
        loginSuccess = True
        break
    
    if loginSuccess:
        print('로그인 성공')
    else:
        print('로그인 실패')
    
    if menu == 3:
        loginId = input('ID입력: ')
        loginPw = input('PW입력: ')

