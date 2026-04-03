import random 


screat = random.randint(0,100) 
attempts = 0 

while(True):
    num  = int(input("Enter your number "))
    attempts += 1 
    if(num == screat):
        print("total attempts need :", attempts ) 
        print("You have successfully guessed the correct number")
        break 

    elif(num < screat):
        print("you number is smaller than screat number.")
    else:
        print("Your number is greater than screat number.")


