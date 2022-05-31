from dotenv import dotenv_values
from twilio.rest import Client

config = dotenv_values('.env')

client = Client(
    config.get('SID'),
    config.get('AUTHTOKEN')
)