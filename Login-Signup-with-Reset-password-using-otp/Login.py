def login():
    while 1:
        uS=input('Enter your username:')
        chck_uS = d.get(uS)
        if chck_uS == None:
            return 'Username not found'
        else:
            pS=input("""
            Enter 0 to reset password.
            Enter your password:""")
            if pS=='0':
                mob=input("""
                You will receive a otp
                Enter your mobile number:""")
                chck_mob(mob)
                otp=input("enter your otp:")
                chck_otp(otp)
                pS=input("Enter new password:")
                chck_pS(pS,uS)
                return 'password changed, login again'
            if pS!='0':
                if chck_uS == pS:
                    return 'Login Successful'
                    break
                else :
                    return 'Entered incorrect password, retry login'
