import random
top_of_range=input("Type a number:")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print("please type a larger number than 0 next time")
        quit()
else:
    print("please type a number next time")
    quit()
random_number=random.randint(0,top_of_range)
quesses=0
while True:
    quesses+=1
    user_quess=input("Make a guess:")
    if user_quess.isdigit():
        user_quess=int(user_quess)
    else:
        print("please type a number next time")
        continue
    if user_quess==random_number:
        print("you got it!")
        break
    elif user_quess>random_number:
        print("you were above the number!")
    else:
        print("you were below the number")
print("you got it in ", quesses,"guesses")
