#!/usr/bin/env python3

import re

message = 'The Hurricane is '

while True:
  Air =input("What is current  wind speed in MPH? ")
 
  if Air != "" and Air !=" " :
      break


Air1 = re.findall("\d+", Air)

wind = float(Air1[0])

if wind >= 70:
   message = message + 'category Five.'
elif wind >= 58:
   message = message + 'category Four.'
elif wind >= 50:
   message = message + 'category Three.'
elif wind >= 43:
   message = message + 'category Two.'
elif wind >= 33:
   message = message + 'category One.'
elif wind <= 32:
  message = message + 'no longer comming'
else:
    message = "Please entre winds speed to identify the hurricane catagory"

print(message)
