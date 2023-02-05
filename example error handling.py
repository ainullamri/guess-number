print("How many cats do you have?")

numCats = input()

try:
    if int(numCats) >= 4:
        print("Thats a lot of cats")
    elif int(numCats) < 0:
        print("You can't have a minus cats")
    else:
        print("That not a lot of cats")

except ValueError:
    print("You are not inputing a number") #if the user input string "six") its value error
    

    
