#Aiden Allison 
#11/14/23
#Working with functions

def get_year():
    #get year from user
    year = int(input("Enter a year to determine if it's a leap year: "))
    return year
def divide_by_4(year):
    if year % 4 == 0:
        return True
    else:
        return False
def divide_by_100(year):
    if year % 100 == 0:
        return True
    else:
        return False
def divide_by_400(year):
    if year % 400 == 0:
        return True
    else:
        return False
def output_results(leap_status,year):
    if leap_status == True:
        print(f"{year}- is a leap year")
    else:
        print(f"{year}- is not a leap year")
def main():
    #create a boolean var to hold leap year status
    is_leap = False

    input_year = get_year()

    if divide_by_4(input_year):                           #does year divide by 4
           #does year divide by 100
        if divide_by_100(input_year):   #does year divide by 400
            if divide_by_400(input_year):
                is_leap = True
            else :
                is_leap = False  #Does Not dvide by 400 
        else :
            is_leap = True #Does Not dvide by 100 
    else :
        is_leap = False #Does Not dvide by 4

    #Print output to user
        
    output_results(is_leap, input_year)

#call the main function
main()
