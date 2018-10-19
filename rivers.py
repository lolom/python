world_rivers = {
  'egypt': 'nile',
  'colombia': 'rio bogota',
  'france': 'seine',
  'serbia': 'danube',
  }

for country, river in world_rivers.items():
  print('The {} runs on {}'.format(river.title(), country.title()))

print('The countries in this list are:')
for country in world_rivers.keys():
  print('{}'.format(country.title()))

print('The rivers in this list are:')
for river in world_rivers.values():
  print('{}'.format(river.title()))