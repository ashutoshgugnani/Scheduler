from twilio.rest import Client 
account_sid = 'ACdff1e1aff8c519c12ca3cb42e8c83c39'
auth_token = 'cf1774ad6ae29812080bf243aa1556f7'
client = Client(account_sid, auth_token)
def send_rem(date,rem):
        message = client.messages.create(  
        from_ = 'whatsapp:+14155238886',
        body='*REMIMDER* '+date+'\n'+rem,
        to='whatsapp:+919766768325'
    )

print(message.sid)