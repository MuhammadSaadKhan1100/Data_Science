# _4th_ Project Pokemon Adventure game 🦊🐸🦄
* Code:
```python
print("    Welcome to Pokemon World 🦄🐆🐬🐓🐠🐥    ")
print("         Player 1-1         ")
name = input("Your Good name: ")
print("Asalamoalikum", name)
opt = input("Do You want to play the game?  ")
if opt != "yes":
    quit()
answer = input("where do you want to go left or right?  ").lower()
if answer == "left":
    print("You came across a river now u can either swim or walk back")
    answer = input("What would you like to do?  ")
    if answer == "swim":
        print("Oh no while swimming Lapras ate u ❗❗")
    elif answer == "walk":
        print("Beedril attacked you and now u r tossed You loser😣😣")

elif answer == "right":
    print("You came across Professor Oak's laboratory , choose your starter charmander or squirtle")
    answer = input("What would you like to choose?  ")
    if answer == "squirtle":
        print("Yes, Great choice 👍👍")
    elif answer == "charmander":
        print("Oh no Charmander evolved into a charmeleom and burnt the whole laboratory🥵🥵")
    else:
        print("Choose from the given ones !!")
else:
    print("Wrong way bro team rocket attacked you")

```
* Output:
![image](https://user-images.githubusercontent.com/112848881/189542807-5ff90531-6c08-4cac-8d80-8615fd7cda28.png)

# _5th_ Project Password Management:
* Code:
```python
from cryptography.fernet import Fernet

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return  key


pwd = input("Dear User please enter master password:  ")

key = load_key() + pwd.encode()
fer = Fernet(key)
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

# write_key()

def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user , passw = data.split("|")
            print("User: ", user, " | Password: ", fer.decrypt(passw.encode()).decode())

def add():
    name = input(" Account name:  ")
    pwd = input("  Password:  ")

    with open('passwords.txt','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    inpt = input("Welcome to Saad Computing software, would you like to (add,view) password or press q to quit  ")
    if inpt == "q":
        break
    elif inpt == "add":
        add()
    elif inpt == "view" :
        view()
    else:
        print("Invalid info")
        continue
```
* Output:
![image](https://user-images.githubusercontent.com/112848881/189544353-2e025153-51d8-4075-893b-0b9e510f7104.png)

🔚
