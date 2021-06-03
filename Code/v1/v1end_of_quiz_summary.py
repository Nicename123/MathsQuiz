score = 0

#Question 1

print("\nQuestion: 1 | score: {}".format(score))
ans=input("6 + 6?\na.10\nb.12\nc.36\nd.Your Answer is:  : ")
if ans == '12' or ans == '12' or ans == 'B' or ans == 'b':
    print('Correct!!!!!')
    score +=1
else:
    print('Incorrect')
    if score <=0:
        score =0

#Question 2
print("\nQuestion: 2 | score: {}".format(score))
ans=input("9 + 9 x 3?\na.36\nb.9\nc.36\nd.Your Answer is:  : ")
if ans == '36' or ans == '36' or ans == 'C' or ans == 'c':
    print('Correct!!!!!')
    score +=1
else:
    print('Incorrect')
    if score <=0:
        score =0

#Question 3
    print("\nQuestion: 3 | score: {}".format(score))
    ans=input("6 - 5?\na.1\nb.11\nc.30\nd.Your Answer is:  : ")
    if ans == '1' or ans == '1' or ans == 'A' or ans == 'a':
        print('Correct!!!!!')
        score +=1
    else:
        print('Incorrect')
        if score <=0:
            score =0

#Question 4
print("\nQuestion: 4 | score: {}".format(score))
ans=input("5 x 7?\na.-2\nb.12\nc.35\nd.Your Answer is:  : ")
if ans == '35' or ans == '35' or ans == 'C' or ans == 'c':
    print('Correct!!!!!')
    score +=1
else:
    print('Incorrect')
    if score <=0:
        score =0

#Question 5
print("\nQuestion: 5 | score: {}".format(score))
ans=input("2 + 2?\na.4\nb.5\nc.3\nd.Your Answer is:  : ")
if ans == '4' or ans == '4' or ans == 'A' or ans == 'a':
    print('Correct!!!!!')
    score +=1
else:
    print('Incorrect')
    if score <=0:
        score =0
print("Thank You -user name- -user age-, for playing my quiz")
print("Your score is", score)
