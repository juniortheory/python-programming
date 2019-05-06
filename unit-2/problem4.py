'''
#problem 4
a = str(input('What caculation would you like to do? Add, Subtract, Multiply or Divide: '))
if 'Add' == a:
    print('Add!')
    b = int(input('What number would you like to Add?: '))
    c = int(input('What other number would you like to Add?: '))
    print('Your total is:', (b + c))
elif 'Subtract' == a:
    print('Subtract!')
    b = int(input('What number would you like to Subtract?: '))
    c = int(input('What other number would you like to Subtract?: '))
    print('Your total is:', (b - c))
elif 'Multiply' == a:
    print('Multiply!')
    b = int(input('What number would you like to Multiply?: '))
    c = int(input('What other number would you like to Multiply?: '))
    print('Your total is:', (b * c))
elif 'Divide' == a:
    print('Divide!')
    b = int(input('What number would you like to Divide?: '))
    c = int(input('What other number would you like to Divide?: '))
    print('Your total is:', (b / c))
'''
#teacher
op = input('What calculations would you like to do? ')
num1 = int(input('Enter first number:  '))
num2 = int(input('Enter second number:'))

if op == 'add':
    res = 'Your result is {}. Calc you later!'.format(num1 + num2)

print(res)

if op == 'add':
    ans = num1 + num2

print(f'Your result is {ans}. Calc you later!')
