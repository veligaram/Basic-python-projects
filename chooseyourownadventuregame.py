name=input("Enter your name :")
print("welcome to the game ",name,"!")
answer=input("you are on a dirt road , it has come to an end and you can go left or right. which way would you like to go ? :").lower()
if answer=="left":
    answer=input("you come to a river, you can walk around or you can swim accross :")
    if answer=="swim":
        print("you swam across and got eaten by a alligator!")
    elif answer=="walk":
        print("you walked for many miles, ran out of water and you lost the game")
    else:
        print("not an valid option you lost!")
elif answer=="right":
    answer=input("you came to a bridge, it looks woobly, do you want to cross it or head back(cross/back) ? ")
    if answer=="back":
        print("you gone back and lost the game")
   elif answer=="cross":
       answer=input("you cross the bridge and meet a stranger . do you want to talk to them(yes/no) ? ")
       if answer=="yes":
           print("you talked to the stranger he gave you gold, YOU WIN")
       elif answer=="no":
           print("you didn't talk to the stanger , he got affended, you lose")
       else:
           print("not a valid option you lost!")
else:
    print("not an valid option you lose")
print("Thankyou for playing the game")
