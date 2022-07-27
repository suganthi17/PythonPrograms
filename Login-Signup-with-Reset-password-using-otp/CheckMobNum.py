def chck_mob(mob):
    if len(mob)==10: 
        snd_msg(mob)
        return
    if mob.isalpha() or mob.isalnum() or len(mob)<10:
        print("invalid mobile number")
        mob=input("enter 10 digit mobile number")
        chck_mob(mob)
