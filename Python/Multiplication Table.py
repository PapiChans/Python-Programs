print('--------------------------')
print('Multiplication Table')
print('--------------------------')

mcd = int(input('Enter a Multiplicand: '))

mtr = int(input('Enter the range of Multiplier'))

print("Here's the result")

for mtr in range(1,mtr+1):
    pdt = mcd * mtr
    print(mcd,'X',mtr,'=',pdt)