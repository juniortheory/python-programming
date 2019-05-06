'''
name = str(input("Enter your name:"))
age = int(input("Enter your age: "))
year = str((2014 - age)+100)
print(name + " will be 100 years old in the year " + year)
'''


age = int(input("Enter your age:"))
if age > 18:
    print("You can watch Rated R movies")
    print("Such as...")
    print("A.) John Wick")
    print("B.) John Wick 2")
    print("C.) Deadpool")
    print("D.) Logan")
#movie = int(input("Which of these movie would you like to see? Select by Letter")
'''

#if movie = "A":
    #print("Great Movie")
#elif movie = "B":
    #print("Great Movie but you should see the first one")
#else:
    #print("Movies are good but John Wick is better")
elif age >= 13:
    print("You can watch PG-13 Movies")
else:
    print("You can watch PG Movies")


word = str(input("Enter Word:"))
word_score =  {
    1: "A, E, I, O, U, L, N, R, S, T",
    2: "D, G",
    3: "B, C, M, P",
    4: "F, H, V, W, Y",
    5: "K",
    8: "J, X",
    10: "Q, Z",
}
print(word_score)
'''
'''
print("Would you like to play a game Charlene?")

from __future__ import print_function

choices = []

for x in range (0, 9):
    choices.append(str(x + 1))

playerOneTurn = True
winner = False

def printBoard() :
    print( '\n ----' )
    print( '|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
    print( '|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print( '|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
    print( ' ----\n' )

while not winner :
    printBoard()

    if playerOneTurn :
        print("Player 1:")
    else :
        print("Player 2:")

    try:
        choice = int(input(">> "))
    except:
        print("please enter a valid field")
        continue
    if choices[choice - 1] == 'X' or choices [choice-1] == 'O':
        print("Illegal move, please try again")

    if playerOneTurn :
        choices[choice - 1] = 'X'
    else :
        choices[choices -1] = 'O'
    playerOneTurn = not playerOneTurn

    for x in range (0, 3) :
        y = x * 3
        if (choices[y] == choices[(y + 1)] and choices [y] == choices[(y + 2)]) :
            winner = True
            printBoard()
        if (choices[x] == choices[(x + 3)] and choices [x] == choices[(x + 6)]) :
            winner = True
            printBoard()

        if((choices[0] == choices [4] and choices[0] == choices [8]) or (choices[2] == choices[4] and choices[4] == choices[6])) :
            winner = True
            printBoard()

print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n")
'''









