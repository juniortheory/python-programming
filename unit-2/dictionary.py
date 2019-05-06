
#dictionary
students = {}

#add to dictionary
students['name'] = 'John'

print(students)

students['name'] = 'Martha'

print(students)

students['courses'] = ['Python programming', 'Data Science', 'UX', 'Social Marketing']

print(students)

my_dictionary = {
    'puppy': 'Furry, energetic aniaml',
    'pineapple': 'Acidic tropical fruit',
    'tea': 'herb-infused drink'

}
print(my_dictionary)

my_dictionary = {}
my_dictionary['puppy'] = 'Furry, energetic animal'
my_dictionary['pineapple'] = 'Acidic tropical fruit'
my_dictionary['tea'] = 'herb-infused drink'

print(my_dictionary)

collection_2 = {"three": 3, "five": 5, 9: "nine"}

print(collection_2)

#model a playlist

my_song = {}

#each song on the playlist
#genre - can be a list
#artist - this can be a list
#album - string
#release_year - string
#title - string
#playback_length - string
#playlist is a list of dictionaries

my_song['genre'] = 'RnB'
my_song['artist'] = '112'
my_song['title'] = 'Only You', 'Dance With Me', 'Peaches N Cream'
my_song['release_year'] = '1999', '2000', '2001'
my_song['playback_length'] = '2:30', '3:30', '4:30' 

print(my_song)

my_playlist = []
my_song = {
    'genres': ['Pop', 'Hip Hop',],
    'artists': ['Katy Perry', 'Jay-Z'],
    'album': 'Life and Times',
    'Title': ['Glory', 'PSA'],
    'playback_length': '2:15'
}

my_playlist.append(my_song)
print(my_playlist)

#swapping positions
a_list = [1, 2, 15, 20]
def swap_first_two(mylist):
    value1 = a_list[0]
    value2 = a_list[1]
    a_list[0] = value2
    a_list[1] = value1
    return(a_list)




swap_first_two(a_list)
print(a_list)

#swapping positions the shorter way

def swap_first_two(mylist):
    mylist[0], mylist[1] = mylist[1], mylist[0]
#pass by reference
a_list = [1, 2, 15, 20]
swap_first_two(a_list)
print(a_list)


def swap_first_two(mylist):
    mylist[0], mylist[1] = 10, 20

a_list = [1, 2, 15, 20]
swap_first_two(a_list)
print(a_list)


my_name = {'R': 1, 'O': 1, 'S':2}
for items in my_name.keys():
    print('The letters {} appears in my name {}'.format(items, my_name[items]))

for letter, val in my_name.items():
    print('The letters {} appears in my name {}'.format(letter, val))

#word frequency generator
def frequency_generator(a_string):
    #returns the number of times each word
    # appears in the string
    pass

#my_sentence = 'There is a man with a plan. The man has the plan in hand'.
#frequency_generator(my_sentence)
#There: 1
#is:1
#a: 3
#man: 3
#with: 1
#plan: 2
#has: 1
#in: 1
#hand: 1

#dictionary can be used in the exercise



