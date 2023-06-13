# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
len_1 = len('python')
len_2 = len('dragon')
print(len_1 < len_2)

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = 'I hope this course is not full of jargon.'
print('jargon' in sentence)

# There is no 'on' in both dragon and python
print('on' not in 'dragon' and 'on' not in 'python')

# Find the length of the text python and convert the value to float and convert it to string
text = 'python'
print('The length of text is ', len(text))
print(float(len(text)), type(float(len(text))))
print(str(len(text)), type(str(len(text))))