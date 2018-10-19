my_pizzas = ["peperoni", "mushroom", "pineapple"]
friend_pizzas = my_pizzas[:]

my_pizzas.append("chocolate")
friend_pizzas.append("strawberries")

for pizza in my_pizzas:
  print("I like " + pizza + " pizza")
  print("I can eat 10 of those pizzas.\n")

print("Man, I really love pizza!\n")

for friend_pizza in friend_pizzas:
  print("\nMy friend likes " + friend_pizza)