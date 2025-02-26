names = ['Amanda', 'Mercedes', 'Rachel', 'Elisabeth', 'Tay', 'Xavier', 'Joaquin', 'Sam']
 
for name in names:
  if 'm' in name.lower():
      continue
  elif 'r' in name.lower():
      pass
  elif 'j' in name.lower():
      break
  else:
       print(name)
