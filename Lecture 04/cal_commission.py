keep_gonig = 'y'
while keep_gonig == 'y':
    sales = float(input('Enter the sales amount: '))
    commission_rate = float(input('Enter the commission rate (as a decimal): '))
    commission = sales * commission_rate
    print(f'The commission is: ${commission:.2f}')
    keep_gonig = input('Do you want to calculate another commission? (y/n): ')