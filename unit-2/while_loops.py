#lesson: Loops

#print a message 10 times
'''
count = 0
while count < 10:
    print('inside while loop')
    count += 1

#search for value in list
nums = [2, 4, 6 , 8, 10]
#found = False
key = 6

while not found:

    if key in nums:
        found = True
        break
if nums[pos]

for idx, item in enumerate(nums):
    print(idx)
    if nums[idx] == key:
        print('Found {} at position {}'.format(key, idx))
        break

#continue
my_nums = [1, 3, 15, 8, 7, 24, 6, 5, -1]
for num in my_nums:
    if num % 2 == 0:
        continue
    print(f'is odd'.format(num))

number = [1, 10]
answer = 2
guess = int(input('Guess a number between 1 and 10:'))

for guess in number:
    if guess == 1:
        continue
    print('Guess Again')
    elif guess >=3:
        continue
    print('Guess Again')
    elif answer == 2:
        print('Correct')

answer = 7
user_input = None

while True:
    user_input = int(input('Enter a number: '))
    if user_input > answer:
        print('Too High')
    elif user_input < answer:
        print('Too Low')
    else:
        print('You got it')
        break
'''
    
#find the sum of a list of numbers

ages = [25, 39, 45, 41, 27, 18, 33, 65, 11, 50]

total_age = 0
for age in ages:
    total_age += age #sum = sum + age

print('Total age is {}'.format(total_age))