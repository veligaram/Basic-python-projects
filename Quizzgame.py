print("Welcome to my quizz game <^>")

playing=input("Do you want to play? ")

if playing.lower()=="yes":
    quit()
print("ok! Let's play the game :)")
score=0
answer=input("What does CPU stands for? ")
if answer.lower()=="central processing unit":
    print("correct!")
    score+=1
else:
    print("Incorrect")
answer=input("What does WHO stands for? ")
if answer.lower()=="world health organisation":
    print("correct!")
    score+=1
else:
    print("Incorrect")
answer=input("What does MLA stands for? ")
if answer.lower()=="member of legustative assembly":
    print("correct!")
    score+=1
else:
    print("Incorrect")    
answer=input("India lifted 2nd world cup on which year? ")
if answer.lower()=="2011":
    print("correct!")
    score+=1
else:
    print("Incorrect")
print("you got " +str(score) +" questions correct!")
print("you got " +str((score/4)*100) +"%.")
