#/Gary Machorro
#8/13/17
#Project2:Problem 1
import random
secret_number=random.randint(1,100)
valid=False
numAttempts=0
while not valid and numAttempts<3:
    numAttempts=numAttempts+1
    try:
        x=15
        attempts=5
        for attempt in range(attempts):
            guess=int(input("Enter your guess:"))
            if guess>=0 and guess<=100:
                x=10
                if guess < secret_number:
                    print('Higher...')
                elif guess > secret_number:
                    print('Lower...')
                else:
                    print("YOU WIN!")
                    break
            else:
                break
        if guess==secret_number:
            break
        elif guess != secret_number and x==10:
            print("You used too many tries!You Lose!")
            print('The secret number was', secret_number)
            break
        elif x==15:
            print("Invalid:Try Again")
        
    except ValueError:
        print("Invalid:Try Again")
    if numAttempts==3:
        print("Program closed due to bad inputs")

#OUTPUTS
'''
Enter your guess:10
Higher...
Enter your guess:12
Higher...
Enter your guess:50
Higher...
Enter your guess:53
YOU WIN!
>>> 
Enter your guess:-1
Invalid:Try Again
Enter your guess:1000
Invalid:Try Again
Enter your guess:D
Invalid:Try Again
Program closed due to bad inputs
>>> 
'''
    
