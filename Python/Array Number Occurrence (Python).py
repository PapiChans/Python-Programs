print('--------------------------')
print('Search a number in an array')
print('--------------------------')

sze = int(input('How many elements in a array?: '))

num = []
for sze in range(0,sze):
    i = int(input('Enter elements in array: '))
    num.append(i)

print('The list of an array: ',num)

sch = int(input('Enter the number you want to search: '))

print('There are',num.count(sch), 'Occurrence/s on number',sch)