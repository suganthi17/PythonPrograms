import re
def chck_mob(mob):
    x = re.search("[0-9]{10}", mob)
    if x:
        print("valid phone number")
        snd_msg(mob)
        return
    else :
        print("Invalid phone number")
        mob=input("enter 10 digit mobile number")
        chck_mob(mob)
