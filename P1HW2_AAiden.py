#9/26/23
#Input,output,expressions

print("this program calculates and displays travel expenses")

budget= int(input("Enter Budget: "))

travel_location= (input("Enter your travel location: "))

gas= int(input("Enter Gas Budget: "))

hotel= int(input("Enter Hotel Budget: "))

food= int(input("Enter Food Budget: "))

expensives = gas+hotel+food
print ("-----------travel expenses-----------")
print("location: ", travel_location)
print("Initial Budget:",budget)
print()
print("Gas:",gas)
print("Hotel:",hotel)
print("Food:",food)
print()
print("Remaining Balance:", budget - expensives)
