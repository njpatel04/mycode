#!/usr/bin/env python3
while True:
    num1 = input("Provide First Number: ")
    try:
        num1 = int(num1)
        break
    except:
        print("This is not a number")

while True:
    num2 = input("Provide Second Number: ")
    try:
        num2 = int(num2)
        break
    except:
        print("This is not a number")
   
while True:        
    operation = input("Provide oprator for caculation '+, -, /, *': ")
    if operation == "+" or operation == "-" or operation == "/" or  operation == "*":
       break


def add(x, y):
    sum = x + y
    return sum

def multi(x, y):
    multi = x * y
    return multi

def devide(x, y):
    dvd = x / y
    return dvd

def sub(x, y):
    sub = x - y
    return sub

if operation == "+":
    print(str(num1) + " + " + str(num2) + " = ", add(num1, num2))
elif operation == "*":
	print(str(num1) + " * " + str(num2) + " = ", multi(num1, num2))
elif operation == "/":
	print(str(num1) + " / " + str(num2) + " = ", devide(num1, num2))
elif operation == "-":
	print(str(num1) + " - " + str(num2) + " = ", sub(num1, num2))

