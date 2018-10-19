names = ["gloria", "ana", "admin"]

if not names:
    print("this list needs more users")
else:
  for name in names:
    if name != "admin":
      print("Hello %s, thanks for login again" % (name.capitalize()))
    elif name == "admin": 
      print("Hello %s, would you like to see your reports?" % (name))

current_users = ["gloria", "ana", "laura", "brandon", "derrick"]

new_users = ["Gloria", "Elton", "Gigi", "Kyle", "Diego", "DERRICK"]

for new_user in new_users:
  if new_user.lower() in current_users:
    print("%s username already exist" % (new_user))
  else:
    print("%s username is available" % (new_user))  