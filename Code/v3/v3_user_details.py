def name(): #Function To Ask For Name
    while True:
        name = input("Enter Your Name : ")
        if name.isalpha():
            break
        print("Please Only Enter Letters")
name()

def age(): #Function To Ask For Age
    while True:
        age = (input("Please Write Your Age : "))
        if age.isnumeric():
            break
        print("Please Only Enter Numbers")
age()
