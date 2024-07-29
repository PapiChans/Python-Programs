print('--------------------------')
print('Search a number in Array')
print('--------------------------')

sze = int(input('How many elements in a array?: '))

num = []
for sze in range(0,sze):
    i = int(input('Enter elements in array: '))
    num.append(i)

print('The list of an array: ',num)

cnt = 0
sch = int(input('Enter the number you want to search: '))

for sze in range(0,sze):
    if sch in num:
        cnt = 1

if cnt == 1:
    print('The number ',sch,' found on the array')
else:
    print('The number ', sch, ' is not on the array')