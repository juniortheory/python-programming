
def high_low():
    my_varaible = 10
    if my_varaible > 10:
        print('HIGH')
    else:
        print('LOW')

def high_low(my_var):
    if my_var > 10:
        print('HIgh')
    else:
        print('Low')

high_low(5)
high_low(12)
high_low(14)
high_low(53)
high_low(55)
high_low(5)


def fizzbuzz():
    for num in range(1,102):
        if num%15 == 0:
            print(num, 'FizzBuzz')
        elif num%5 == 0:
            print(num, 'Buzz')
        elif num%3 == 0:
            print('Fizz')
        else:
            print(num)
fizzbuzz()

def capitalize(my_name):
    #convert to uppercase
    return my_name.upper()

print(capitalize('ross bautista'))


def add_two(number):
    total = number + 2
    print(total)
    return total


def cap_first_letter(sentence):
    new_sentence = ''
    for word in sentence.split(' '):
        new_word = word[0].upper() + word[1:]
        # create new sentence with new words
        #no spaces
        #new_sentence += new_word + ' '
        #adding a space
        new_sentence += new_word + ' '
    return new_sentence

print(cap_first_letter('Split this string up'))





