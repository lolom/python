alien_0 = {'x_position': 0, 'y_position': 0, 'speed': 'fast'}
print("Original x-position: {}".format(alien_0['x_position']))

#move alien to the right
#Determine how far move the alien based on current speed
if alien_0['speed'] == 'slow':
  x_increment = 1
elif alien_0['speed'] == 'medium':
  x_increment = 2
else:
  x_increment = 3

#the new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: {}".format(alien_0['x_position']))      
