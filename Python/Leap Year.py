print('--------------------------')
print('Leap Year')
print('--------------------------')
year = int(input('Enter a Year: '))

if(((year % 4 == 0) and (year % 100!= 0)) or (year% 400 == 0)):
    print('--------------------------')
    print('The year', year, 'is a leap year')
    print('--------------------------')

else:
    print('--------------------------')
    print('The year', year, 'is not a leap year')
    print('--------------------------')