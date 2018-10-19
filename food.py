my_food = ["mushrooms", "peanut sauce", "ribs", "ice cream", "chorizo"]
friends_food = my_food[:]
my_food.append("falafel")
friends_food.append("pizza")

for one_food in my_food:
 print("My favourite food is: " + one_food) 

for friend_one_food in friends_food:
  print("\nMy friend's favourite food is: " + friend_one_food) 

print("\nThe first three items of my food are:")
print(my_food[:3])

print("\nThe middle three items of my food are:")
print(my_food[2:5])

print("\nThe last three items of my food are:")
print(my_food[3:])

