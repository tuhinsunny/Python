#R , P , S
import random
user_points=0
computer_points=0
times_of_play=int(input('How many times do you want to play? : '))
for i in range(times_of_play):
    user = input("Enter the Input (R/P/S): ").upper()
    comp = random.choice(['R','P','S'])
    print("-------------------------------------------------------------------------------------------------------------------")
    print(f"User choose: {user} and Computer choose: {comp}")
    if (user=='R' and comp=='S') or (user=='S' and comp=='P') or(user=='P' and comp=='R'):
        print("User won!!")
        user_points+=1
    elif(user=='S' and comp=='R') or (user=='P' and comp=='S') or(user=='R' and comp=='P'):
        print("Computer won!!")
        computer_points+=1
    else:
        print("Match Draw")
    print(f"User Score: {user_points} and Computer Score: {computer_points}")
    print("-------------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------")
if(user_points>computer_points):
    print("User won the game!!!!!!")
elif(user_points<computer_points):
    print("Computer won the game!!!!!!")
else:
    print("Match is drawn. Nobody won the Game!!!")
print("-------------------------------------------------------------------------------------------------------------------")