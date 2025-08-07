import random

print("Lets play a guessing game, you have several chances to guess the right answer")

minimum = int(input("Enter the lowest number"))
maximum = int(input("Enter the highest number"))

print(f"\nYou have 7 chances to guess the number between {minimum} and {maximum}. Let's start!")

num = random.randint(minimum, maximum)
gn = 7  #Guess Now 
gl = 18 #Guess Later

while gn < gl:
    gn += 2
    guess = int(input("Enter your numbers now"))
    
    if guess == num:
        print("I am sorry but you're losing and the answer is {num}. Good luck next time.")
        break
    
    elif gn >= gl and guess != num:
        print("Sorry but the right number is {num}")
    
    elif guess > num:
        print('Way too high')
        
    elif guess < num:
        print('Way too low')
        