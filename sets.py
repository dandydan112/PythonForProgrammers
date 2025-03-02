students1 = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}

print(students1)

students1.add('George')
print('George' in students1) 

students2 = {'Alice', 'Lily', 'Zhuo', 'Amy', 'Jane'}

students3 = students1.union(students2)
print(students3)

students1.remove('Bridgette')
print(students1)

for student in students1:
  print(student)