#!/usr/bin/env python3

astro = {"number": 3, "message": "success", "people": [{"craft": "ISS", "name": "Chris Cassidy"}, {"craft": "ISS", "name": "Anatoly Ivanishin"}, {"craft": "ISS", "name": "Ivan Vagner"}]}

print("People in space: "+ str(astro["number"]) + "\n")

i = 0

for x in astro:
    print(astro["people"][i]["name"] + " is on the " + astro["people"][i]["craft"])
    i = i + 1
