class ClassSchedule:
   def __init__(self, course):
       self.course = course

   def __del__(self):
       print('You successfully deleted your schedule')
 
first = ClassSchedule('Chemistry')
print(first.course)

del first

print(first.course)
