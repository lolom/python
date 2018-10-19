toppings = ["mushrooms", "onions", "pineapple"]
"mushrooms" in toppings
"peperoni" in toppings
if toppings != "anchovies":
  print("Hold the anchovies!")

requested_toppings = ["mushrooms", "extra cheese", "green pepper"]
  
for requested_topping in requested_toppings:  
  if requested_topping == "green pepper":
    print("Sorry, we are out of peppers")
  else:  
    print("Adding %s. " % (requested_topping))    
  
print("Finished pizza.")

requested_toppings1 = []

if requested_toppings1:
  for requested_topping in requested_toppings1:  
      print("Adding %s. " % (requested_topping))    
  print("Finished pizza.")
else: 
  print("are you sure you want plain pizza?")
    