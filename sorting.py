favorite_language = {
  'jen' : 'python',
  'David' : 'Ruby',
  'Damian' : 'html',
  'Camilo' : 'js',
  'Lorena' : 'c'
}

for name in sorted(favorite_language.keys()):
  print('Thanks for taking the poll {}'.format(name.title()))