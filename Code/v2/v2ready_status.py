#Ask If They Are Ready To Take The Quiz
status = input("Are You Ready To Take The Quiz? \na. Yes \nb. No \n=>")

# What if the user is not ready
if status == 'No' or status == 'no' or status == 'b' or status == 'B':
    print("See You Next Time.")

# What if the user is ready?
if status == 'Yes' or status == 'yes' or status == 'A' or status == 'A':
    print("Welcome To The Quiz.")
