#Aiden Allison 
#10/19/23
#Working with if else statements

#create a boolean var to hold leap year status
is_leap = False

#Get year from user
input_year = int(input("Enter a year to find leap year!: "))

                                #does year divide by 4
if input_year % 4 == 0:         #does year divide by 100
    if input_year % 100 == 0:   #does year divide by 400
        if input_year % 400 == 0:
            is_leap = True
            print(is_leap) 
        else :
            is_leap = False  #Does Not dvide by 400 
    else :
        is_leap = True #Does Not dvide by 100 
else :
    is_leap = False #Does Not dvide by 4

#Print output to user
    
if is_leap == True:
    print(f"{input_year}- is a leap year")
else:
    print(f"{input_year}- is not a leap year")
