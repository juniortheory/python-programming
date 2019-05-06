'''
def cap_first_letter(sentence):
    new_sentence = ''
    for word in sentence.split(' '):
        new_word = word[0].upper() + word[1:]

        new_sentence += new_word + ' '
    return new_sentence

print(cap_first_letter('hi how are you'))
'''
def fizzbuzz():
    for num in range(1,102):
        if num % 15 == 0:
            print(num, 'fizzbuzz')
        elif num % 5 == 1:
            print('fizz')
        elif num % 3 == 1:
            print('bizz')

fizzbuzz()