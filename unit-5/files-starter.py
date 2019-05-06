import re
#with regular expression
def find_and_replace(file_name, find_what, replace_with):
    with open(file_name, 'r') as f:
        old_story = f.read

    new_story = re.sub(find_what, replace_with, old_story)
    print(new_story)

#reading a file
f = open('short_story.txt', 'r')
data = f.read()

#always close the file after opening
f.close()

print(data)

#writing a file (over writes the text)

f = open('short_story.txt', 'w')
f.write('This is now a new story\n')
f.write('And this is the second line\n')
f.close()

#append to a file
f = open('short_story.txt', 'a')
f.write('This is the new line in my story\n')
f.write('The End')
f.close()

#seek to specific positions and overwrite
f = open('short_story.txt', 'r+')
f.seek(11)
f.write('Overwrite this here')
f.close()

#so we don't have to close each time we open
with open('short_story.txt', 'w') as f:
    f.write('This is a short story\n')
    f.write('This story is very short\n')
    f.write('This is now the end because it is short.')

'''
def find_and_replace(file_name, file_what, replace_with):
    file = open(file_name, 'r')
    data = ('short_story', 'r')
'''

line = 'This is a short story.'
find_what = 'short'
replace_with = 'good'
find_idx = line.find('sh')
print(find_idx)

part_before = line[:find_idx] #copy from start of line to the found position
part_after = line[find_idx + len(find_what):] #copy from found position + length of
                                              #search string to end of line
print(part_before)
print(part_after)

new_line = ''

new_line += part_before + replace_with + part_after
print(new_line)