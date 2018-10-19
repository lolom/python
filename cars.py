cars = ['bmw', 'audi', 'toyota', 'subaru', 'mercedes']
cars.sort(reverse=True)
print(cars)

cars_two = ['bmw', 'audi', 'toyota', 'subaru', 'mercedes']
print('here is the original list: ') 
print(cars_two)
print('\nhere is the sorted list:')
print(sorted(cars_two, reverse=True))
print('\nhere is the original list again:')
print(cars_two)