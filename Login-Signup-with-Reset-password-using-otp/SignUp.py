d={} #initialize dictionary once

def signUp():
    while 1:
        uS = input("""
        Enter 0 to Exit, else,
        Enter new Username: """)
        if uS == "0":
            print('Exiting Signup...')
            return 'Failed'
        elif uS not in d:
            pS = input("""
            password must contain 8 characters.
            password must contain atleast one number.
            Enter a strong password:
            """)           # passwordStrength()
            print(chck_pS(pS,uS))
#             if len(pS)>=8 and pS.isalnum() :
#                 d.update({uS:pS})              # d[uS] = pS
#                 return 'Successful'
#             else:
#                 return 'Password Strength is weak'
        else:
            print('Username exists. Please try again...')

