from twilio.rest import Client

TWILIO_ACCOUNT_SID = 'ACc2f9e7534a3fb59daee030069146b740'
TWILIO_AUTH_TOKEN = 'ef02356a38f8aa77e60c3aaeb9f010e1'

def send(phone_number, epoch, success):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    if success:
        client.messages.create(
            to="+82"+phone_number,
            from_="+12512702122",  # twilio에서 발급받은 미국 전화번호
            body="^_^[성공] {}번째 Epoch".format(epoch)
        )
    else:
        client.messages.create(
            to="+82" + phone_number,
            from_="+12512702122",  # twilio에서 발급받은 미국 전화번호
            body="0o0[실패] {}번째 Epoch".format(epoch)
        )
if __name__ == '__main__':
    send('01059118952', '2', True)
