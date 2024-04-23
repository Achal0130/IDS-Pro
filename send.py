from twilio.rest import Client

account_sid = 'AC6de654825ba3267605c803789cc638bd'
auth_token = 'e93c21ef39d2181a95955e8d50e22279'
client = Client(account_sid, auth_token)

def sendsms():
    sender_number = '+13345084519'  # Changed variable name to avoid conflict
    message = client.messages.create(
        from_=sender_number,  # Used from_ instead of from
        body='Alert',
        to='+918329898145'
    )

sendsms()