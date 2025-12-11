def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

ch = input("Choose Operation: + or - or * or /: ")
print("Result: ")
if ch == "+":
    print(add(a,b))
elif ch == "-":
    print(sub(a,b))
elif ch == "*":
    print(mul(a,b))
else:
    print(div(a,b))
    