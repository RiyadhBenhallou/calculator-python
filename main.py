from replit import clear
from art import logo

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y


def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

operations = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '/': divide
}

# print(logo)


def calculator():
  finished_calculating = False
  x = float(input('What\'s the first number: '))
  while not finished_calculating:
    for symbol in operations:
      print(symbol)
    op = input('Which operation you want to perform from above: ')
    y = float(input('What\'s the next number: '))

    result = operations[op](x, y)
    clear()
    print(f'{x} {op} {y} = {result}')
    answer = input(f'Type "yes" If you want to use {result} in another calculation, type "no" to start a new calculation, type "1" if you want to exit: ')
    if answer == 'no':
      calculator()
    elif answer == 'yes':
      x = result
    else:
      finished_calculating = True
  
calculator()

print('Thanks for using Pythonista')