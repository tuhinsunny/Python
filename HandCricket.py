import random
print("Let the Toss begin")

user=input("User choose whether Odd or Even : ")
user1=int(input("Play a number from 1 to 6 : "))
comp1=random.choice([1,2,3,4,5,6])
print("User chooses",user1,"and computer chooses",comp1)
if(user1+comp1)%2==0 :
    result="Even"
else:
    result="Odd"
if (user=="Even" and result=="Even") or (user=="Odd" and result=="Odd"):
    print("User won the toss! Do you want to Bat or Ball ?")
    us1=input()
    if(us1=="Bat"):
        us2="Ball"
    else:
        us2="Bat"
else:
    print("Computer won the toss")
    us2=random.choice(["Bat","Ball"])
    print("Computer chooses to",us2)
    if(us2=="Bat"):
        us1="Ball"
    else:
        us1="Bat"
user_score=0
computer_score=0
u=int(input("Enter a number between 1 to 6 : "))
c=random.choice([1,2,3,4,5,6])
print("User chooses",u,"and Computer chooses",c)
if us1=="Bat":
    user_score+=u
    if u==c:
        user_score=0
    while u!=c:
        u=int(input("Enter a number between 1 to 6 : "))
        c=random.choice([1,2,3,4,5,6])
        print("User chooses",u,"and Computer chooses",c)
        user_score+=u
    if(user_score!=0):
        user_score=user_score-u
    print("User is out ! Now it's computer's turn!!")
    print("Computer needs",(user_score+1),"runs to win the game")
    c=random.choice([1,2,3,4,5,6])
    u=int(input("Enter a number between 1 to 6 : "))
    print("Computer chooses",c,"and User chooses",u)
    if u==c:
        computer_score=0
    while c!=u and computer_score<=user_score:
        u=int(input("Enter a number between 1 to 6 : "))
        c=random.choice([1,2,3,4,5,6])
        print("Computer chooses",c,"and User chooses",u)
        computer_score+=c
    if computer_score > user_score:
        print("Computer won the match")
    else:
        print("User won the match")
else:
    computer_score+=c
    if u==c:
        computer_score=0
    while c!=u:
        u=int(input("Enter a number between 1 to 6 : "))
        c=random.choice([1,2,3,4,5,6])
        print("Computer chooses",c,"and User chooses",u)
        computer_score+=c
    computer_score=computer_score-c
    print("Computer is out ! Now it's user's turn!!")
    print("User needs",(computer_score+1),"runs to win the game")
    c=random.choice([1,2,3,4,5,6])
    u=int(input("Enter a number between 1 to 6 : "))
    print("User chooses",u,"and Computer chooses",c)
    if u==c:
        user_score=0
    while c!=u and user_score<=computer_score:
        u=int(input("Enter a number between 1 to 6 : "))
        c=random.choice([1,2,3,4,5,6])
        print("User chooses",u,"and Computer chooses",c)
        user_score+=u
    if user_score > computer_score:
        print("User won the match")
    else:
        print("Computer won the match")