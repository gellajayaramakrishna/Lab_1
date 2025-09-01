# simple calculator with basic operations

def add(a,b):
    return a+b

def subtract(a,b):
 return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
 if b==0:
     print("Error: Division by zero")
 else:
     return a/b


def main():
    print("Available operations: add, subtract, multiply, divide")
    while True:
        op = input("Enter operation: ").lower()
        if op=="quit":
            print("Bye");break
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if op=="add":
         print(add(num1,num2))
        elif op=="subtract":
            print(subtract(num1,num2))
        elif op=="multiply":print(multiply(num1,num2))
        elif op=="divide":
            print(divide(num1,num2))
        else:print("Invalid operation")

main()
