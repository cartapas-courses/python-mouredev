# Day 03

age = 38
height = 1.75
complex = (3 + 4j)

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
print('====== TRIANGLE 1 =======')
base = input('Enter base: ')
height = input('Enter height: ')
print('The area of the triangle is ', float(base) * float(height) * 0.5)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c)
print('====== TRIANGLE 2 =======')
side_a = input('Enter side a: ')
side_b = input('Enter side b: ')
side_c = input('Enter side c: ') 
print('The perimeter of the triangle is ', float(side_a) + float(side_b) + float(side_c))