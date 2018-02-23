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

team_gen = input("Would you like to specify team names? ").lower()
if team_gen == "yes" or team_gen == "y":
  alt_teamA = input("\nWhat would you like to call Team A? ").title()
  alt_teamB = input("What would you like to call Team B? ").title()
else:
  alt_teamA = "Team A"
  alt_teamB = "Team B"
  
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
print(alt_teamA + ": ", end='')
for i in range(0, len(teamA)):
  print(teamA[i], end=' || ')
print("\n\n" + alt_teamB + ": ", end='')
for i in range(0, len(teamB)):
  print(teamB[i], end=' || ')
