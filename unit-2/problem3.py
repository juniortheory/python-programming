'''
#problem 3
user_entry = str(input('Enter a word or sentence:'))
print(user_entry[::-1])
'''
#teacher(Good for reserving lists)
sentence = input('Enter a sentence: ')
'''
res = ''
last_idx = len(sentence) - 1
while last_idx >= 0:
    res += sentence[last_idx]
    last_idx -= 1

print(res)
'''
#reversing a string
print(''.join(reversed(sentence)))

# ''.join (joins objects together) 