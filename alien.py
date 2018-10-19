alien_0 = {}
print(alien_0)

alien_0['color'] = 'green' 
alien_0['points'] = 5
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print("alien color is now %s" % (alien_0['color']))

alien_0['color'] = 'yellow'
print("alien color is now %s" % (alien_0['color']))



new_points = alien_0['points']

print("You have just made %s points" % (new_points))

del alien_0['points']
print(alien_0)