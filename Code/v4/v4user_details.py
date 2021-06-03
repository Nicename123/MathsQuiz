def name(): #To ask for user's name
    global name
    while True:
        name = input("Enter Your Name : ")
        if name.replace(' ','').isalpha():
            break
        print("Please Only Enter Letters") #Error message if user enters anything other than letters
name()

def age(): #To ask for user's age
    global age
    while True:
        age = (input("Please Write Your Age : "))
        if age.isnumeric():
            break
        print("Please Only Enter Numbers") #Error message if user enters anything other than numbers 
age()

print("Hello", name, "aged", age)
