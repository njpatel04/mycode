#!/usr/bin/env python3

message = "The "

char_name = input(" Which character do you want to know about? (Flash, Batman, Superman): ")
char_stat = input(" What statistic do you want to know about? (strength, speed, or intelligence): ")

char_name = char_name.lower()
char_stat = char_stat.lower()  

info = {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "highest", "strength": "money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}


if char_name == "flash" and char_stat =="speed":
   message = message + char_name + '\'s ' + char_stat + ' is: ' +  info["flash"]["speed"]
   
elif char_name == "flash" and char_stat =="intelligence":
   message = message + char_name + '\'s ' + char_stat + ' is: ' +  info["flash"]["intelligence"]

elif char_name == "flash" and char_stat == "strength":
   message = message + char_name + '\'s ' + char_stat + ' is: ' +  info["flash"]["strength"]

elif char_name == "batman" and char_stat == "speed":
   message = message + char_name + '\'s ' + char_stat + ' is: ' +  info["flash"]["speed"]
   
elif char_name == "batman" and char_stat == "intelligence":
   message = message + char_name + '\'s ' + char_stat + ' is: ' +  info["flash"]["intelligence"]

elif char_name == "batman" and char_stat == "strength":
   message = message + char_name + '\'s ' + char_stat + ' is: ' +  info["flash"]["strength"]
   
elif char_name == "superman" and char_stat == "speed":
   message = message + char_name + '\'s ' + char_stat + ' is: ' +  info["flash"]["speed"]
   
elif char_name == "superman" and char_stat == "intelligence":
   message = message + char_name + '\'s ' + char_stat + ' is: ' +  info["flash"]["intelligence"]

elif char_name == "superman" and char_stat == "strength":
   message = message + char_name + '\'s ' + char_stat + ' is: ' +  info["flash"]["strength"]  
   
   
print(message)
