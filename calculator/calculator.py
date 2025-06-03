#Creating calculator with command line arguments

import sys

def add(num1, num2):
    return (num1 + num2)

def sub(num1, num2):
    return (num1 - num2)

def mul(num1, num2):
    return (num1 * num2)

def div(num1, num2):
    return (num1 / num2)

operation = sys.argv[1]
num1 = float(sys.argv[2])
num2 = float(sys.argv[3])

if operation == "add":
    output = add (num1, num2)

elif operation == "sub":
    output = sub (num1, num2)

elif operation == "mul":
    output = mul (num1, num2)

elif operation == "div":
    output = sub (num1, num2)

else:
    print ("Result is not found") 

print("Result:", output)  #print the results

Terminal: python calculator.py add 10 12  #to get the output
