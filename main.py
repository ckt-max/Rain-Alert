import requests
import json
import os
from twilio.rest import Client

twilio_recovery_code = 'BNVRFUBL1CVY2USAHP5PZTPU'

#twilio credentials
account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_TOKEN')
client = Client(account_sid, auth_token)

# getting data via owm api
owm_endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
key = os.environ.get('OWM_API_KEY')
weather_params = {
    'lat':28.704060,
    'lon':77.102493,
    'appid': key,
    'cnt': 4
}
response = requests.get(owm_endpoint, params= weather_params)
print(response.status_code) # status code helps to check if api is working properly
weather_data = response.json()
# print(weather_data)

# checking if its going to rain in the next 12 hours and sending a notification if it does
if (weather_data['list'][0]['weather'][0]['id'] or
    weather_data['list'][1]['weather'][1]['id'] or
    weather_data['list'][2]['weather'][2]['id'] or
    weather_data['list'][3]['weather'][3]['id']) in range(500,600):
    message = client.messages.create(
        from_= os.getenv('TWILIO_NO'),
        body="Hi, it's going to rain today. Don't forget your umbrella",
        to='+919654958647'
    )

    print('Rain alert sent')

else:
    # message = client.messages.create(
    #     from_='+18586836682',
    #     body="Don't worry pal. You can leave your umbrella back at home",
    #     to='+919654958647'
    # )
    print("It's not going to rain. No SMS sent")

