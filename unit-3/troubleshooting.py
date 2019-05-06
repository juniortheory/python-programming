'''
fruits = ['apple', 'pear', 'orange']

rapper = {
    'name': 'Young Thug'
    'address': 'No idea'
    'hit': 'none'
}

#print(rapper['telephone'])

class Student:
    def __init__(self, name):
        self.name = name

a = Student('John')

a.grade = 50

print(a.grade)


try:
    val = int(input("enter a number: "))
except ValueError as ve:
    print('You didnt enter a numer', ve)
'''



class Phone:
  def __init__(self, phone_number):
    self.number = phone_number

  def call(self, other_number):
    print("Calling from", self.number, "to", other_number)

  def text(self,  other_number, msg):
    print("Sending text from", self.number, "to", other_number)
    print(msg)
new_phone = Phone(5214)

test_phone = Phone(414)
test_phone.call(515)
test_phone.text(int("text 141"), "Hi!")