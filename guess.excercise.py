guess_names = []
guess_names.append('Isadora Duncan')
guess_names.append('Marie Curie')
guess_names.append('Frida Khalo')
guess_names.append('La Pola')

not_comming = 'Isadora Duncan'
guess_names.remove(not_comming)

guess_names.append('Ada Lovelace')

print(len(guess_names))

print("You have been invited to Lorena's dinner party dear: " + guess_names[0])
print("You have been invited to Lorena's dinner party dear: " + guess_names[1])
print("You have been invited to Lorena's dinner party dear: " + guess_names[2])
print("You have been invited to Lorena's dinner party dear: " + guess_names[3])


print(not_comming)

guess_names.insert(0, 'Isadora Duncan')
guess_names.insert(0, 'Pocahontas')
guess_names.append('Mulan')

print(len(guess_names))

print("You have been invited to Lorena's dinner party dear: " + guess_names[0])
print("You have been invited to Lorena's dinner party dear: " + guess_names[1])
print("You have been invited to Lorena's dinner party dear: " + guess_names[2])
print("You have been invited to Lorena's dinner party dear: " + guess_names[3])
print("You have been invited to Lorena's dinner party dear: " + guess_names[4])
print("You have been invited to Lorena's dinner party dear: " + guess_names[5])
print("You have been invited to Lorena's dinner party dear: " + guess_names[6])

uninvited_guess = guess_names.pop(0)
print("You have been uninvited, sorry dear " + uninvited_guess)

uninvited_guess = guess_names.pop(0)
print("You have been uninvited, sorry dear " + uninvited_guess)

uninvited_guess = guess_names.pop(0)
print("You have been uninvited, sorry dear " + uninvited_guess)

uninvited_guess = guess_names.pop(0)
print("You have been uninvited, sorry dear " + uninvited_guess)

uninvited_guess = guess_names.pop(0)
print("You have been uninvited, sorry dear " + uninvited_guess)

print(guess_names)
print(len(guess_names))

print("You still invited to Lorena's party, dear: " + guess_names[0])
print("You still invited to Lorena's party, dear: " + guess_names[1])

guess_names.remove('Ada Lovelace')
guess_names.remove('Mulan')

print(guess_names)

print(len(guess_names))