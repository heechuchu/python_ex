from config_dir import config
from member import session
from db import member_db
from member import member_dumy
if config.DEV_MOD:
    member_dumy.memberDumyInit()
    print(f'memberDB: {member_db.memberDB}')


flag = True

while flag: 
    
    menuNum = ''
    if session.signInedMemberId == '': # sign in 상태
        menuNum = int(input('1.sign-up  2.sign-in  3.modify  4.delete 5.sign_out 99.end'))
    else: #sign out상태
        menuNum = int(input('3.modify  4.delete 5.sign_out 99.end')) 
   
    if menuNum == config.SIGN_UP:
        print('1.sign-up')
        uId = input('please input new member ID: ')
        uPw = input('please input new member PW: ')
        uMail = input('please input new member MAIL: ')
        uPhone = input('please input new member PHONE: ')

        member_db.memberDB[uId] = {
            'uId' : uId,
            'uPw' : uPw,
            'uMail' : uMail,
            'uPhone' : uPhone
        }
        print('New member sign-up success!!')
        
        if config.DEV_MOD:
            print(f'memberDB: {member_db.memberDB}')
                 


    elif menuNum == config.SIGN_IN:
        print('2.sign-in')
        uId = input('please input member ID: ')
        uPw = input('please input member PW: ')

        if uId in member_db.memberDB:
            if member_db.memberDB[uId]['uPw'] == uPw:
                print('sign-in success!!')
            else:
                 print('sign-in fail ! --  pw error')

        else:
            print('sign-in fall ! -- Id error')

    elif menuNum == config.MEMBER_MODIFY:
        print('3.modify')
    
    elif menuNum == config.MEMBER_DELETE:
        print('4.delete')

    elif menuNum == config.MEMBER_DELETE:
        print('99.end')
        flag = False
        
    elif menuNum == config.SIGN_OUT:
        print('5.sign_out ')
