# Strings formatting
first_name = 'Matias'
last_name = 'Tapasco'
language = 'Python'

formated_string = 'My son is %s %s. He wish to study %s' %(first_name, last_name, language)
print(formated_string)

# Strings and numbers formatting
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius %d is %.2f.' %(radius, area)
print(formated_string)

python_libraries = ['Django', 'Flask', 'Numpy', 'Matplotlib', 'Pandas']
formated_string = 'The following are python libraries:%s' %(python_libraries)
print(formated_string)