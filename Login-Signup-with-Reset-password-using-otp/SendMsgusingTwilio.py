# importing twilio
from twilio.rest import Client
import random
# Your Account Sid and Auth Token from twilio.com / console
account_sid = 'AC2c510651ed843ca3dfb50e729db4b9a9'
auth_token = 'b07a78b4bf07269462056ce7d2990f6d'

client = Client(account_sid, auth_token)


''' Change the value of 'from' with the number
received from Twilio and the value of 'to'
with the number in which you want to send message.'''
def snd_msg(mob): 
    s = ""
    for x in range(6):
        n = random.randint(0,9)
        ns = str(n)
        s += ns
    message = client.messages.create(
							from_='+19704787068',
							body ="your Otp is:" + s,
							to ='+91'+mob
						)
    
