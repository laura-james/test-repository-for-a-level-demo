import random
file_object = open('example-question-file.txt', 'r')
#print(file_object.read())
#lines=file_object.readlines()
lines=file_object.read().splitlines() 
score=0
quizlength=10
#loop round 5 times
for num in range(1,quizlength+1): 
    #get random question
    question=random.randrange(0, 140, 6)
    #rpnt question - so +1
    print(lines[question+1])
    #print 4 answers
    print("A: " + lines[question+2])
    print("B: " + lines[question+3])
    print("C: " + lines[question+4])
    print("D: " + lines[question+5])

    #take in answer
    answer = input("")
    #print("You said "+answer)
    if answer.upper()==lines[question]:
        print("Correct!")
        score=score+1
    else:
        print("Wrong! It was "+lines[question])

print("You scored "+str(score)+" out of "+str(quizlength))
# todo: check if question has been asked before - if so choose another question
#C could add a quit option?
# could calculate percentage score
#could write top scorers to a file
