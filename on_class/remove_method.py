students = ['julia', 'alex', 'alex', 'alex', 'alina', 'alex', 'kristi', 'alex', 'alex', 'alex']
number = 0
for i in students:
    if i.__eq__('alex'):
        number=number+1

for i in range(number):
    students.remove('alex')

print(students)
