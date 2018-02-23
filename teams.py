from random import choice
from termcolor import colored

players = []
teamA = []
teamB = []
x = 1

total = input("How many players are there in total? ")
if int(total) % 2 == 1:
  print(colored("\n[CAUTION]! The number of players you have chosen is odd. That forces one team to have more players than the other.", 'red'))
  print()
else:
  print()
  
while x <= int(total):
  invite = input("Player #" + str(x) + ": ").title()
  players.append(str(invite))
  x += 1

while len(players) > 0:
  playerA = choice(players)
  teamA.append(playerA)
  players.remove(playerA)
  
  if len(players) != 0:
    playerB = choice(players)
    teamB.append(playerB)
    players.remove(playerB)

print()
print("Team A: ", end='')
for i in range(0, len(teamA)):
  print(teamA[i], end='\t')
print("\n\nTeam B: ", end='')
for i in range(0, len(teamB)):
  print(teamB[i], end='\t')
