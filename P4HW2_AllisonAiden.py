#Aiden Allison 
#11/2/23
#If else caculater

#User display 
print("Employee pay caculater")
#Declareing Total Vars
Total_E = int(0) 
Total_OT = float(0) 
Total_RH = float(0) 
Total_GP = float(0)
#Start of Loop
name = input("Enter the name of employee or 'DONE' to terminate: ")
while name != "DONE":
#input from user
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
    #Actual pay caculaters
    Total_E += 1
    Total_OT += overPayAmount
    Total_RH += amountPay
    Total_GP += grossPay
    #output
    print(f"Employee name: {name}")
    print("------------------------------------------------------------------------------------------------------------------------------------")
    print(f"Hours worked: {hour} Pay Rate: {pay} Overtime {overtime} OverTime Pay {overPayAmount} RegHour pay {amountPay} Gross Pay {grossPay}")
    print("------------------------------------------------------------------------------------------------------------------------------------")
    name = input("Enter the name of employee or 'DONE' to terminate: ")
else:
   print(f"Total number of employees entered:{Total_E} Total amount paid for overtime:{Total_OT} Total amount for regular hours:{Total_RH} Total amount paid in gross:{ Total_GP }")
    
