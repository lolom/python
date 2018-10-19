for value in range(1, 21):
  print(value)

million = list(range(1, 1000000))

print(min(million))
print(max(million))
print(sum(million))  

for odd_number in range(2, 20, 2):
  print(odd_number)

for multiple_three in range(3, 30, 3):
  print(multiple_three)

cubes = [cube**3 for cube in range(1, 10)]
print(cubes)
