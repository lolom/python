banned_users = ["andrew", "carolina", "david"]
user = "andrew"

if user not in banned_users:
  print(user.title() + ", you can post if you wish!")
else:
  print(user.title() + ", nope!")  