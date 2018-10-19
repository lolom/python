favorite_language = {
  'jen' : 'python',
  'David' : 'Ruby',
  'Damian' : 'html',
  'Camilo' : 'js',
  'Lorena' : 'js'
}

for name in sorted(favorite_language.keys()):
  print('Thanks for taking the poll {}'.format(name.title()))

for name, language in favorite_language.items():
  
  if language == 'html' or language == 'js':
    print("{} favorite language is {}.".format(name.title(), language.upper()))
  else:
    print("{} favorite language is {}.".format(name.title(), language.title()))


friends = ['jen', 'david'] 
for name, language in favorite_language.items():
  print('{}'.format(name.title()))

  if name.lower() in friends:
    print('hey {} it seems like your favorite language is {}'.format(name.title(), language.title()))

if 'erin' not in favorite_language.keys():
  print('Please take your survey Erin')

for language in set(favorite_language.values()):
  print('{}'.format(language.title()))
