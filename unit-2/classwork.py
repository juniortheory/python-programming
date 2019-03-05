#Lesson: Lists
classmates = ["Ross", "Marcus", "Flavio", "Joseph", "Maham", "Vinay", "Gungeet", "Faris"]

#prints number of items in the list
print(len(classmates))
#prints the first item in the list ("0" is the first item(Ross),"7" is the eighth item on the list)
print(classmates[0])
#print the last item on the list
print(classmates[-1])

#adds an element to the list
classmates.append("John")

print(classmates[-1])
print(classmates[1])

#inset an element into the list
classmates.insert(1, "Jane")
print(classmates[1])

#remove an element from the list
classmates.pop(-1)


#print all elements in the list
for name in classmates:
    print(name)
'''
#search item in the list
for name in classmates:
    if name == 'Maham':
        print('Maham found in list')
'''

if 'Maham' in classmates:
    print('Found Maham in the List!!')

#using indices in for loop(finding the position in the list)
for idx, name in enumerate(classmates):
    print(idx, name)

#reverse order the list
surname = 'Bautista'

for x in range(len(surname)-1, -1, -1):
    print(surname[x])

#shortest way to reverse order the list
print(surname[::-1])

