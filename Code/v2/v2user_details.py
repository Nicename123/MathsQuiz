
#Quiz User details
print("Welcome To The Maths Qiuz")
print("This quiz is developed by Vrishank")

#The following code is to Ask User For Details

while True:
    name = input("Enter Your Name : ")
    if name.isalpha():
        break
    print("Please Only Enter Letters")
while True:
    age = (input("Please Write Your Age : "))
    if age.isnumeric():
        break
    print("Please Only Enter Numbers")

#The function of print will show the details

print("Hello", name)
print("You are", age, "years old")


