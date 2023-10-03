#name
#10/3/2023
#dse floats and expressions to caculate gas cost


#create input var
mpg = float(input("Enter Cars gas milage: "))
dollarspgallon = float(input("Enter Cost of gas: "))

#caculate gas cost off of gallons needed,price per gallon

cost_20=(20/mpg) * dollarspgallon
cost_75=(75/mpg) * dollarspgallon
cost_500=(500/mpg) * dollarspgallon
#output are values using an f string and format the floats
print(f"{cost_20:.2f} {cost_75:.2f} {cost_500:.2f}")
