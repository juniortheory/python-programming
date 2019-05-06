#problem 2.1
statement = 'Hi There!'
count = 0
num = 4
while count < num:
    print(statement)
    count += 1

#problem 2.2
number = 2
my_list = [1, 2, 3, 4]
for num in my_list:
    print(num * number)

factor = 3
my_nums = [2, 4, 6, 8, 10, 12]

for idx in range(len(my_nums)):
    my_nums[idx] = my_nums[idx] * factor