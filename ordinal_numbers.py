ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for ordinal_number in ordinal_numbers:
  if ordinal_number == 1:
    print("%sst" % (ordinal_number))
  elif ordinal_number == 2:
    print("%snd" % (ordinal_number))
  elif ordinal_number == 3:
    print("{}rd".format(ordinal_number))  
  else: 
    print("{}th".format(ordinal_number))  