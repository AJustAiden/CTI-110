#Name
#10/5/23
#Formatting floats


#input float values 
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

#defining variables that caculate expressions 
num_product = num1*num2*num3*num4
num_average = (num1+num2+num3+num4)/4

#output of basic expressions using f string
print(f'{num_product:.0f}')
print(f'{num_average:.3f}')
