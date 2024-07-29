print('--------------------------')
print('Find the Factorial of the number')
print('--------------------------')

num = int(input('Enter a number: '))
fct = 1

print(' ')
print('--------------------------')
print('The formula to find the factorial is:')
print('Factorial * Count')

for i in range(num,0,-1):
     fct = fct * i

print('The factorial of ',num,'is ',fct)

