weight = int(input('Enter your weight in kilograms: '))
height = float(input('Enter your hight in meters: '))

bmi = (weight / (height * height))
print('Your BMI is : ' , format(bmi, '.2f'))
