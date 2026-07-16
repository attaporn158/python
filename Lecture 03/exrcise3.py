#hours = int(input("Enter the number of worked: "))
#pay_rate = int(input("Enter the pay rate: "))
#gross_pay = hours * pay_rate
#print("Gross pay: $", gross_pay)

hours = int(input("Enter the number of worked: "))
pay_rate = float(input("Enter the pay rate: "))
if hours > 40:
    gross_pay = (40 * pay_rate) + ((hours - 40) * (pay_rate * 1.5))
else:
    gross_pay = hours * pay_rate
print("Gross pay: $", gross_pay)