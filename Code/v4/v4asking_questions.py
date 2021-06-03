score = 0
correct = 0
incorrect = 0

mathquiz = [
[
    "What is 5 + 5",
    {'answer':'b','option':'a)0\nb)10\nc)25\nd)11\n'}#Q1
    ],
[
    "What is 9 + 9 x 3",
    {'answer':'c','option':'a)54\nb)26\nc)36\nd)27\n'}#Q2
    ],
[
    "What is 2 + 2",
    {'answer':'b','option':'a)0\nb)4\nc)1\nd)22\n'}#Q3
    ],
[
    "What is 9 squared",
    {'answer':'d','option':'a)3\nb)99\nc)92\nd)81\n'}#Q4
    ],
[
    "What is the cube root of 27",
    {'answer':'a','option':'a)3\nb)9\nc)16\nd)24\n'}#Q5
    ],
[
    "What is 4 - 7",
    {'answer':'b','option':'a)11\nb)-3\nc)44\nd)3\n'}#Q6
    ],
[
    "What is 12 + 12",
    {'answer':'c','option':'a)144\nb)0\nc)24\nd)122\n'}#Q7
    ],
[
    "What is 7 x 8",
    {'answer':'a','option':'a)56\nb)15\nc)-1\nd)78\n'}#Q8
    ],
[
    "What is 9 + 10",
    {'answer':'b','option':'a)21\nb)19\nc)90\nd)0.9\n'}#Q9
    ],
[
    "6 x 9 + (6 + 9)",
    {'answer':'a','option':'a)69\nb)54\nc)44\nd)59\n'}#Q10
    ],
]

print("****************************************************")
def gamerounds():
    global g
    while True:
        try:
            g=int(input("\nHow many rounds do you want to play : ")) #Asking the user how many rounds they want to play
            if 0<g<=10:
                break
            else:
                print("Chose numbers between 1 and 10") #If user chooses a number = to or less than 0 or a number more than 10
        except:
           print('Only enter digits for number rounds please (The maximum is 10)') #Error message if user chooses a number = to or less than 0 or a number more than 10
gamerounds()

while g>0:
    data = mathquiz[0]
    q = data[0]
    data =data[1]
    answer = data['answer']
    option = data['option']

    print(q)
    print(option)
    while True:
        answers = input("Please enter your answer here : ").lower().replace(' ','')
        if answers =='a' or answers == 'b' or answers == 'c' or answers == 'd':
            if answers == answer:
                print("********************************************************************************************************************")
                print("You answered correctly") #If user answers correctly
                print("********************************************************************************************************************")
                score +=1 #When user answers correctly
                correct +=1 #When user answers correctly
                print("---------------------------------------------------------------------------------------------------------------------")
                print("your score is",score)
                print("---------------------------------------------------------------------------------------------------------------------")
            else:
                print("********************************************************************************************************************")
                print("Sadly you answered incorrectly. The correct answer is ",answer)    
                print("********************************************************************************************************************")
                incorrect +=1 #When user answers incorrectly
                print("---------------------------------------------------------------------------------------------------------------------")
                print("your score is",score)
                print("---------------------------------------------------------------------------------------------------------------------")

            del mathquiz[0]
            g-=1
            break
        else:
            print("please enter the alphabet for the chosen option") #If user doesn't answer with a letter
