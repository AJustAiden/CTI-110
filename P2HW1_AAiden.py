# Your Name   
# 10/5/23
# Introduction to dictionaries



#defining var for dict
HeightVar = float(input("What is your height? "))
AgeVar = int(input("What is your age? "))


#defining dict and rest of keys 
user_traits = {
    
"FristName" : input("What is your first name? "),
"HairColor" : input("What is your hair color? "),
"EyeColor" : input("What is your eye color? "),
"HeightFeet" : HeightVar,
"Age"           : AgeVar ,
"FavoriteFood" : input("What is your favorite Food? ")

}


#output dict user_traits in F string
print(f'{user_traits["FristName"]} is a {user_traits["HeightFeet"]} tall student with {user_traits["HairColor"]} and {user_traits["EyeColor"]}. They are {user_traits["Age"]} and their favortie food is {user_traits["FavoriteFood"]} ')
