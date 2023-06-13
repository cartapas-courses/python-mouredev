# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = input('Enter number to check: ')
print('Is ', number, ' an even number? -> ', (float(number) % 2 ) == 0)

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print('The floor division of 7 by 3 is equal to the int converted value of 2.7? -> ', int(7 // 3) == 2.7)

# Check if type of '10' is equal to type of 10
print(type('10') == type(10))

# Check if int('9.8') is equal to 10
print(int(9.8) == 10)

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = input('Enter the amount of hours worked: ')
rate = input('Enter the payment per hour: ')
print('Your weekly earning is :', float(hours) * float(rate))

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = input('Enter number of years you have lived: ')
print('You have lived for ', int(years) * 365 * 24 * 60 * 60 , ' seconds')

# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
print('Display the following table')
print('1', '1', '1', '1', '1')
print('2', '1', '2', '4', '8')
print('3', '1', '3', '9', '27')
print('4', '1', '4', '16', '64')
print('5', '1', '5', '20', '125')