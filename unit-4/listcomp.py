marvel_movies = ['Captain America, The First Avenger', 'Iron Man', 'Iron Man II',
'Thor', 'Thor, The Dark World', 'The Amazong Spiderman', 'Dr Strange']

'''
create a new list with all the movies without the word 'The' in their title

new_movies = []
for movie in marvel_movies:
    if 'The' not in movie:
        new_movies.append(movie)

print(marvel_movies)
'''

new_movies = []
for movie in marvel_movies:
    if 'The' not in movie:
        new_movies.append(movie)

print(new_movies)

new_movies = [movie for movie in marvel_movies if 'The' not in movie]
print(new_movies)
#list comprehension

#copy old list
fruits = ['apple', 'peach', 'mango']
              #result
copy_fruits = [fruit for fruit in fruits]
              #_____________________
              #iteration

numbers = [2,46,8,10]
new_numbers = [num ** 2 for num in numbers]
print(new_numbers)

vals = [1, 2, 3, 5, 7, 9, 11]
odds = [val for val in vals if val % 2 == 1]

print(odds)

nice_fruit = ['Apple', 'Peaches', 'Pear', 'Mango', 'Kiwi']
new_fruit = [fruit if fruit[0] == 'P' else fruit[0] for fruit in nice_fruit]
print(new_fruit)

#download anaconda
