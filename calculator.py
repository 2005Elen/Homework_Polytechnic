def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "error"
    else:
        return x / y

x = int(input('enter the number 1'))
y = int(input('enter the number 2'))

print('choose an operation: add, subtract, multiply or divide')

a = input()

if a == 'add':
    print(add(x, y))
elif a =='subtract':
    print(subtract(x, y))
elif a =='multiply':
    print(multiply(x, y))
elif a =='divide':
    print(divide(x, y))
else:
    print('error')