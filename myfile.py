'''
grade = 80
if grade > 80:
    print("A")
elif grade >= 60:
    print("B")
else:
    print("C")
'''

from random import randint

answer = randint(1,10)

guess = int(input("please enter your guess: "))

if guess == answer:
    print("You are correct")
else:
    print("try again")
    





