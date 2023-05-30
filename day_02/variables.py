# Day 2: 30 Days of python programming

# Multiple assignment in Python: Assign multiple values or the same value to multiple variables
# https://note.nkmk.me/en/python-multi-variables-values/

# Declare the requested variables
first_name = 'Carlos'
last_name = 'Tapasco'
full_name = 'Marcela Ramirez Arias'
country = 'Colombia'
city = 'Cali'
age = '38'
year = '2023'
is_married = False
is_light_on = True
var1, var2 = 'Value1', 'Value2'

# Check the data type of all your variables
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))
print(type(var1))
print(type(var2))

# Find the length of your first name and your last name
print(len(first_name))
print(len(last_name))

# Compare the length of your first and last name
print('Max lenght:', max(first_name, last_name))
print('Min lenght:', min(first_name, last_name))

# Math
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

math = {
    'Total: ': total,
    'Diff: ': diff,
    'Product: ': product,
    'Division: ': division,
    'Remainder: ': remainder,
    'Exp: ': exp,
    'Floor division: ': floor_division
}
print(math)

# The radius of a circle is 30 m
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
# area = pi * r ^ 2
area_of_circle = 3.1416 * 30.0 ** 2
print(area_of_circle)

# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# circumference = 2 * pi * r
circum_of_circle = 2 * 3.1416 * 30.0
print(circum_of_circle)

# Take radius as user input and calculate the area
radius = input('Enter the value of radius: ')
print(type(radius))
area_of_circle = 3.1416 * float(radius) ** 2
print(area_of_circle)

# Use the built-in function to get first name, last name, country and age from a user and store the value to their corresponding variable names.
first_name = input('First name: ')
last_name = input('Last name: ')
country = input('Country: ')
age = input('Age: ')

user_data = {
    'First name: ': first_name,
    'Last name: ': last_name,
    'Country: ': country,
    'Age: ': age
}

print(user_data)

# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')