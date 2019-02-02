import requests
import datetime

def timediff(city1time, city2time):
  d1 = datetime.datetime.strptime(city1time,"%Y-%m-%d %H:%M:%S")
  d2 = datetime.datetime.strptime(city2time,"%Y-%m-%d %H:%M:%S")
  return (d2-d1)

api_time = 'http://api.timezonedb.com/v2.1/get-time-zone?'
api_key = 'key=J6TSDA7ZWA4F'
api_restofstuff = '&format=json&by=zone&zone=America/'


#Input 1 code
city1 = input("Pick a city: ")

website = api_time + api_key + api_restofstuff + city1

print(website)

city1data = requests.get(website).json()

if city1data['status'] == 'OK':
  print("Status is ok!"),
else :
  print(city1data['message'])

city1time = city1data['formatted']

print(city1data)


#Input 2 code
city2 = input("Pick another city: ")

website2 = api_time + api_key + api_restofstuff + city2

city2data = requests.get(website2).json()

if city2data['status'] == 'OK':
  print("Status is ok!"),
else :
  print(city2data['message'])

city2time = city2data['formatted']

print(city2data)

print(timediff(city1time, city2time))


#Time difference function

#convert string to integer --> typecasting
