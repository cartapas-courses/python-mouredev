
import sys
import numpy as np

# Check version
print(sys.version)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Using the points (0,-2) and (1,0)
# Calculate the Slope in Python. https://www.delftstack.com/howto/python/calculate-slope-python/
# numpy.polyfit. https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html

x = [0, 1]
y = [-2, 0]
slope, intercept = np.polyfit(x,y,1)
print('The slope using numpy library is ', slope)
print('The y intercept is ', intercept)
print('The x intercept is ', 2 / 2)

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
print('The slope using two points is ', (10 - 2) / (6 - 2))
print('The Euclidean distance between the two points is ', ((10 - 2) ** 2 + (6 - 2) ** 2) ** 0.5)