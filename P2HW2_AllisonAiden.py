#Aiden Allison
#10/10/23
#Working with lists


#putting it in the list
grade_list = [
   int(input("What was your test grade for Module_1? ")),
   int(input("What was your test grade for Module_2? "))
]
#create variables and get user input
module3 = int(input("What was your test grade for Module_3? "))
module4 = int(input("What was your test grade for Module_4? "))
module5 = int(input("What was your test grade for Module_5? "))
module6 = int(input("What was your test grade for Module_6? "))
#add method 
grade_list.append(module3)
grade_list.append(module4)
grade_list.append(module5)
grade_list.append(module6)
#caculate min/max sum/average 
grade_min = min(grade_list)
grade_max = max(grade_list)
grade_sum = sum(grade_list)
grade_average = grade_sum/6
#Display info to user/use print statements
print(f"The lowest grade you have is {grade_min}")
print(f"The highest grade you have is {grade_max}")
print(f"The sum of all your grades is {grade_sum}")
print(f"The average of all your grades is {grade_average}")
