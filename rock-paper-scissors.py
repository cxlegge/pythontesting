#a python script for a daft game of rock, paper, scissors

from random import choice

p = input("Choose rock (r), paper, (p) or scissors (s): ")

options = {'r':'Rock', 'p':'Paper', 's':'Scissors'}
moves=["Rock","Paper","Scissors"]

c = choice(moves)

print(options[p] + ' versus ' + c)

if (c == 'Rock' and p == 's') or (c == 'Paper' and p == 'r') or (c == 'Scissors' and p == 'p'):
    print('You got smashed mate.')
elif (c == 'Rock' and p == 'p') or (c == 'Paper' and p == 's') or (c == 'Scissors' and p == 'r'):
    print('You wrecked this computer.')
elif c == options[p]:
  print('It be a draw.')
else:
    print('you did something wrong ya dingus.')
