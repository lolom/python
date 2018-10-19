alien_color = "red"

if alien_color == "green":
  print ("you just earned 5 points")
if alien_color != "green":
  print("you just earned 10 points")

if alien_color == "green":
  print("you just earned 5 points")
else:
  print("you just earned 10 points")  

if alien_color == "green":
  points = 5
elif alien_color == "yellow":
  points = 10
elif alien_color == "red":
  points = 15

print("You just earned %s points" % (points))      

if alien_color == "green":
  points = 5
if alien_color == "yellow":
  points = 10 
if alien_color == "red":
  points = 15

print("You just earned %s points" % (points))

if alien_color == "green":
  points = 5
elif alien_color == "yellow":
  points = 10
else:
  points = 15

print("You just earned %s points" % (points))   