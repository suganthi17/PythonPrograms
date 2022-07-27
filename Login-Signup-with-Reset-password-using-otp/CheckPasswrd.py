def chck_pS(pS,uS):
    while 1:
        if len(pS)>=8 and pS.isalnum():
            d.update({uS:pS})              # d[uS] = pS
            return 'Successful'
            break
        else:
            print('Password Strength is weak, try different password.')
            pS=input("Enter the password:")
            return chck_pS(pS,uS)
