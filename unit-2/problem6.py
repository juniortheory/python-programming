breakfast = ['Fruit Loops', 'Frosted Flakes', 'Cinnamon Toast Crunch']
for name in breakfast:
    print(name, "are yummy!")

#teacher
def do_breakfast():
    breakfast = ['Fruit Loops', 'Wheaties', 'Capn Crunch']
    for br in breakfast:
        if br[-1] == 's':
            print(f'{br} are yummy')
        else:
            print(f'{br} is yummy')

