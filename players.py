players = ["martina", "ana", "pietro", "lorena", "marija"]
print(players[0:3])
print(players[1:4])
print(players[:7])
print(players[2:])
print(players[-3:])

print("Here are the first 3 players of my team:")
for player in players[:3]:
  print(player.title())