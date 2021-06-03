#To ask if user is ready
status = input("\nAre you ready to play the best maths quiz? (Enter Yes Or No): \na. Yes \nb. No \n=>")

#If user is not ready
if status == 'No' or status == 'no' or status == 'b' or status == 'B' or status == 'n' or status == 'N': #If user is not ready
    print("See you later")
    exit()
    
#If user is ready
elif status == 'Yes' or status == 'yes' or status == 'a' or status == 'A' or status == 'y' or status == 'Y': #If user is ready
    print("**************************************************** WELCOME TO MATHS QUIZ ****************************************************")
