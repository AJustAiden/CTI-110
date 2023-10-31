#Aiden Allison
#10/10/23
#Working with lists


#user input
num_grades = int(input("how many test grades will you enter: "))
#create empty list
grade_list = []

for grade in range(num_grades):
        this_grade = int(input("Enter a grade: "))
        #while this_grade >= 0 and this_grade <=100:
        if this_grade > 100 or this_grade < 0:
            print(f"{this_grade} is invalid")
        else:
            grade_list.append(int(this_grade))
    
#caculate min/max sum/average 
grade_min = min(grade_list)
grade_sum = sum(grade_list)
avg = grade_sum/len(grade_list)

if avg >= 90:
     lettergrade="A"
elif avg >= 80:
       lettergrade="B"  
elif avg >= 70:
         lettergrade="C"
elif avg >= 60:
        lettergrade="D" 
else:
       lettergrade="F"
#Display info to user/use print statements



print(f"The lowest grade you have is {grade_min}")
print(grade_list)
print(f"The average score is {avg}")
print(lettergrade)


