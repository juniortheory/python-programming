breakfast = ['Fruit Loops', 'Frosted Flakes', 'Cinnamon Toast Crunch', 'Honey Oats', 'Capn Crunch', 'Oreos', 'Corn Pops', 'Raisin Bran', 'Trix', 'Waffle Crisp', 'Corn Flakes']
for idx, name in enumerate(breakfast):
    if 's' == name[-1]:
        print(name, 'are yummy')
    elif 's' != name[-1]:
        print(name, 'is yummy')



