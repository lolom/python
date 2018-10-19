name = ['marija', 'nina', 'ana', 'vuk']
print(name[0].title())
print(name[1].title())
print(name[2].title())
print(name[-1].title())

print("hello you " + name[0].title())
print("hello you " + name[-1].title())
print("hello you " + name[-2].title())

transportation = ['motorbike', 'bike', 'car', 'transmilenio']
message = "I hate to drive a "

transportation[0] = 'death machine'
transportation.append('motorbike')

print(message + transportation[-1].title())
print(message + transportation[0].title())
print(message + transportation[2].title())
print(transportation)

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('vespa')
motorcycles.insert(-1, 'ducati')

print(motorcycles)

del motorcycles[0]

print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)

print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me" )

first_owned = motorcycles.pop(0)

print(motorcycles)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

