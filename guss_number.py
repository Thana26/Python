import random
name=input("Enter you name:")
print("Hi ",name,"...welcome to the Game of Guesses")
c=input("Do you want to play? Yes or no:")
count=0
if(c=="Yes"):
        n=random.randint(0,10)
        x=int(input("Guess a number between 0 to 10:"))
        while(x!=n):
            if (x>n):
                print("Your number is higher")
                x=int(input("Guess again:"))
                count=count+1
            elif (x<n):
                print("your number is lower")
                x=int(input("Guess again:"))
                count=count+1
        print("You got it right for ",count,"trials")
        print("Thankyou for playing")
else:
        print("Okay...bye!")
