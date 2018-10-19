available_toppings = ["mushrooms", "pepperoni", "peppers", "cheese", "anchovies"]
requested_toppings = ["cheese", "french fries", "mushrooms"]

for requested_topping in requested_toppings:
  if requested_topping in available_toppings:
    print("Adding %s." % (requested_topping))
  elif requested_topping not in available_toppings:
    print("%s is not available in our toppings" % (requested_topping))

print("Finished pizza!")      