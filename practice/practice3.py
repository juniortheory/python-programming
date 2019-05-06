names = ['Ross Bautista', 'RJ Bautista', 'Kristle Bautista']
print('Welcome to the Birthday Dictionary! We know Birthdays of:')
print(*names, sep = '\n')
user_entry = str(input('Whose birthday would you like to know?: '))
for people in names:
    while user_entry != people:
        if user_entry == 'Ross Bautista':
            print('Ross Bautista\'s birthday is June 100th')
        elif user_entry == 'RJ Bautista':
            print('RJ Bautista\'s birthday is March 100th')
        elif user_entry == 'Kristle Bautista':
            print('Kristle Bautista\'s birthday is November 100th')
        elif user_entry != people:
            print('Enter name correctly(Case sensitive)')
            user_entry = str(input('Please enter name again: '))
            continue
        break

