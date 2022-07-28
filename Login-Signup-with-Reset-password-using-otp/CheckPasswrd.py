#import re --if not imported

def chck_pS(pS,uS):
    while 1:
        x1 = re.search("[a-zA-Z]", pS)
        x2 = re.search("[0-9]",pS)
        x3 = re.search("[@,#,$]",pS)
        if x1 and x2 and x3 and len(pS)>=8:
            print("valid password")
            d.update({uS:pS})              # d[uS] = pS
            return 'Successful'
            break
        else:
            print('Password Strength is weak, try different password.')
            pS=input("Enter the password:")
            return chck_pS(pS,uS)
