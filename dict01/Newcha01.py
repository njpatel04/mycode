#!/usr/bin/env python3
easy= ["science", "turbo", ["goggles", "eyes"], "nothing"]


medium= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


hard= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

# print("My " + easy[2][1] +"! " + "The " + easy[2][0] + " do " + easy[3] +"!")

# print("My " + medium[2]["goggles"] +"! " + "The " + medium[2]["eyes"] + " do " + easy[3] +"!")

print("My " + hard[0]["user"]["name"]["first"] +"! " + "The " + hard[0]["kumquat"] + " do " + hard[0]["d"] +"!")
