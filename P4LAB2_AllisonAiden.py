#Aiden Allison
#10/31/23
#Use for loops

#getinput from user
Geninput =int(input("name a integer: "))
maxinput =int(input("name a 2nd integer: "))

#loop itself

if Geninput <= maxinput:
    for item in range (Geninput,maxinput + 1,5):
        print(item)
    else:
         print("rerun program")
