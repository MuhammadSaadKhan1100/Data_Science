# PROJECT#1  General Knowledge Quiz Game:
* Code:
```python
## Small Game Project by Muhammad Saad Khan for Bytewise fellowship
print(" Welcome to Saad Quiz World 🤖🤖")
print("           player  1-1")
ins = input("Do You want to play the quiz game  ").lower()
score = 0
if ins != "yes":
    quit()
else:
    print("Game begins...")
    answer = input("What is the full form of CPU " ).lower()
if answer == "central processing unit":
    print("correct  😁 ")
    score = score + 1
else:
    print("incorrect  😕")
answer = input("What is the full form of GPA ").lower()
if answer == "Grade Point Average":
    print("correct  😁")
    score = score + 1
else:
    print("incorrect  😕")
answer = input("What is the full form of RAM ")
if answer == "Random Access Memory":
    print("correct  😁")
    score = score + 1
else:
    print("incorrect  😕")

print("You Earned a score of: " + str(score))  # Tells the score
percentage = (score/3)*100
print("% age of Answers correct =  " + str(percentage) )  # Tells the percentage of
                                                          # correct answers
```
* Output:
![image](https://user-images.githubusercontent.com/112848881/189409277-a7c17c06-2026-4443-904c-f46127499b91.png)
![image](https://user-images.githubusercontent.com/112848881/189409410-01562eb2-d366-427b-91bf-82a8694e3c2a.png)

# PROJECT#2  Number Guessing game:
. Code:
```python
# 2nd Project Number Guessing Game created by Muhammad Saad Khan
import random
ans = input("Enter The Number: 🐰    ")
if ans.isdigit():
    ans = int(ans)
    if ans <= 0 :
        print("Please enter a digit greater than 0 next time")
        quit()
else:
    print("Please enter a number next time.")
    quit()

r = random.randint(0, ans)
guesses = 0

while True:
    guesses += 1
    guess = input('Guess the number 🙃  ')
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Try a number next time 😥")
        continue

    if guess == r:
        print("You got it right 👍👍")
        print("Number of guesses made: ", guesses)
        break
    elif guess > r:
        print("You are above the number")
    elif guess < r:
        print("You are below the number")
    else:
        print("Try again")
```
* Output:
![image](https://user-images.githubusercontent.com/112848881/189409827-96d3c2df-c0b8-4465-99de-0d2dee20ad4b.png)

# Project#3 Rock, Paper, Scissor game 🥌 📃 ✂:
* Code:
```python
print("-----Welcome to Rock, Paper, Scissor game 🥌 📃 ✂ ----")
print("                 Player 1-1                 ")
import random
user_wins = 0
computer_wins = 0
objects = ["rock","paper","scissor"]
while True:
    user_input = input("Enter rock,paper or scissor  ")
    if user_input == "q" :
        break
    if user_input not in objects:
        continue

    random_number = random.randint(0,2)
    comp_input = objects[random_number]

    if user_input == "rock" and comp_input == "scissor":
        print("You Won 👍👍")
        user_wins += 1
    elif user_input == "paper" and comp_input == "rock":
        print("You Won 👍👍")
        user_wins += 1
    elif user_input == "scissor" and comp_input == "paper":
        print("You Won 👍👍")
        user_wins += 1
    else:
        print("You Lost 😢👎👎")

print("User won",user_wins,"times .")
print("Computer won",computer_wins,"times .")
print("GoodBye 👋")
```
* Output:
![image](https://user-images.githubusercontent.com/112848881/189410607-4a59b88b-a48a-43bc-bff2-c11091ef78e6.png)
🔚
