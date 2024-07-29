print('--------------------------')
print('BMI (Body Mass Index) Calculator')
h1 = float(input('Enter your Height in Centimeters (cm): '))
wei = float(input('Enter your Weight in Kilograms (kg): '))

h2 = h1 / 100
hei = h2 * h2
bmi = wei / hei

print('--------------------------')
print('Computation of your BMI')
print('--------------------------')
print('Your Height is: ',h1,'cm')
print('Your Weight is: ',wei,'kg')

print('To calculate BMI')
print('Height: ',h1,'cm / 100 is ',h2)
print('Square of Height: ',h2,'* ',h2,'is ',hei)
print('Your BMI is Weight divided by Height: ',wei,'/ ',hei)

print('BMI: ',bmi)

if (bmi <= 18.5):
    print('Weight status: Underweight')
elif (bmi <= 24.9):
    print('Weight status: Healthy')
elif (bmi <= 29.9):
    print('Weight status: Overweight')
elif (bmi <= 34.9):
    print('Weight status: Obesity class 1')
elif (bmi <= 39.9):
    print('Weight status: Obesity class 2')
elif (bmi >= 40.0):
    print('Weight status: Obesity class 3')