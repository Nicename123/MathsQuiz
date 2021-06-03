#This Program Will Tell Users Their End Of Quiz Summary


#Questions That Will Be Summarised

correct = 0
incorrect = 0
score = 0

print("\nQuestion: 1 | score: {}".format(score))
ans=input(" Chose Correct Or Incorrect?\na.correct\nb.incorrect\nc.Your Answer is:  : ")
if ans == 'A' or ans == 'a' or ans == 'Correct' or ans == 'correct':
     print('Correct!!!!!')
     print('Correct!!!!!')
     score +=1
     correct +=1
     print("Your Score is", score)
else:
     print('Incorrect')
     if score <=0:
        score =0
        incorrect +=1

print("\nQuestion: 2 | score: {}".format(score))
ans=input(" Chose Correct Or Incorrect?\na.correct\nb.incorrect\nc.Your Answer is:  : ")
if ans == 'A' or ans == 'a' or ans == 'Correct' or ans == 'correct':
     print('Correct!!!!!')
     score +=1
     correct +=1
     print("Your Score is", score)
else:
     print('Incorrect')
     if score <=0:
        score =0
        incorrect +=1

print("\nQuestion: 3 | score: {}".format(score))
ans=input(" Chose Correct Or Incorrect?\na.correct\nb.incorrect\nc.Your Answer is:  : ")
if ans == 'A' or ans == 'a' or ans == 'Correct' or ans == 'correct':
     print('Correct!!!!!')
     score +=1
     correct +=1
     print("Your Score is", score)
else:
     print('Incorrect')
     if score <=0:
        score =0
        incorrect +=1

print("You got", correct, "questions correct and you got", incorrect, "questions incorrect." )
