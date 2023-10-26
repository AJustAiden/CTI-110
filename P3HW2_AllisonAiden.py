#Aiden Allison 
#10/26/23
#If else caculater

#User display 
print("Employee pay caculater")
#input from user
name = input("Enter the name of employee: ")
hour = float(input("Enter the number of hours the employee worked this week: "))
pay = float(input("Enter the employee pay rate: "))
#Overtime caculater
if hour > 40:
    overtime = (hour - 40)
    reghour = 40
else:
    overtime = 0
    reghour = hour
#Actual pay caculaters 
OverPay = (pay*1.5)
amountPay = (reghour * pay)
overPayAmount = (overtime * OverPay)
grossPay = (overPayAmount + amountPay)

#output
print(f"Employee name: {name}")
print(f"Hours worked: {hour} Pay Rate: {pay} Overtime {overtime} OverTime Pay {overPayAmount} RegHour pay {amountPay} Gross Pay {grossPay}")
