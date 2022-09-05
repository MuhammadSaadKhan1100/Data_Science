# Python
Definition:
 Python is a multipurpose programming language mainly used in
 . Machine learning
 . Data Scienece
 . AI
 . Automation
 # First python project
 ```python
 print("Hello World")
 ```
 # Variables
 Variales are used to store data temporarily in computer memory, their values can be changed
 For Example:
 ```python
 age = 20
price = 30.99
name = "Muhammad Saad Khan"
is_online = False
print(age)
print(price)
print(name)
print(is_online)
 ```
 # Exercise
 ```python
 name = "John Smith"
age = 20
ptype = 'New patient'
print(name)
print(age)
print(ptype)
 ```
 # Receiving input
 we can also receive input from the user e.g asking name from the user
 ```python
 name = input("What is your good name? ")
print("Asalamoalikum " + name) #concatenation
 ```
 ![image](https://user-images.githubusercontent.com/112848881/188451853-450bd1f8-e80e-488b-ae11-1d176e1a1775.png)
 # Type conversion
 Sometimes we need to change datatypes i.e int, strings etc . 
 .Example:
 #wrong code:
 ```
 birth_year = input("Dear customer Enter your birthyear ")
age = 2022 - birth_year
print("Your Age is " + age)
 ```
 ![image](https://user-images.githubusercontent.com/112848881/188453730-af2245a0-0d6f-43ce-9f42-e02a07917381.png)
 # Correct code:
 ```python
 birth_year = input("Dear customer Enter your birthyear ")
age = 2022 - int(birth_year)
print(age)
 ```
![image](https://user-images.githubusercontent.com/112848881/188454566-4d1f95e0-92ae-41fc-b41f-0d939df8082f.png)
# Exercise:
```python
# Simple calculator
num1 = input("First ")
num2 = input("Second ")
Sum = float(num1) + float(num2)
print("Sum: " + str(Sum))
```
# Strings:
strings are like real world objects e.g consider a TV remote it has various functionalities
Similarly either you can capitalize, lower, find and append our code to desired thinking
```python
course = 'Python for beginners'
print(course.upper())
```
```python
course = 'Python for beginners'
print(course.lower())
```
```python
course = 'Python for beginners'
print(course.find('y'))
```
```python
course = 'Python for beginners'
print('Python' in course)
```
```python
course = 'Python for beginners'
print(course.replace('for','4'))
```
# Arithmetic operators in Python:
. Addition
. Subtraction
. Multiplication
. Division (float)
. Division (int)
. Remainder %
. Power of **
```python
# Arithmetic operations in code
print(10 + 2) # Addition
print(10 - 3) # Subtraction
print(10 * 2) # Multiplication
print(10 / 2) # Division float
print(10 // 2) # Division int
print(10 % 2) # Remainder
print(10 ** 3) # Raise to the power of
```
# Operator precedences
Python follows DMAS rule means it will perform in following series
. Division
. Multiplication
. Addition
. Subtraction
10+3*2
so answer will be 16

# Comparison Operators
>,>=,<,<+,==,!=
```python
x = 3 > 2
print(x)
```
![image](https://user-images.githubusercontent.com/112848881/188469860-80528872-f0cc-4e56-89fb-04d0d81d8eb4.png)
# Logical operators
```python
x = 10
print(x < 20 and x > 23) # Logic AND
print(x < 20 or x > 23) # Logic OR
```
![image](https://user-images.githubusercontent.com/112848881/188474471-dc60f76c-1d15-473f-b79b-b1ed664e1f50.png)

# if-else Statements:
```python
temperature = 25
if temperature > 35 :
    print("It's a hot day")
elif temperature >= 25:
    print("It's a nice day")
elif temperature < 10:
    print("It's a bit cold day")
print("Done")
```
# Exercise:
```python
weight = float(input("Enter your weight in Kg or Lb "))
typy = input(" K or L? ")
if typy.upper() == 'K' :
    print("Weight in lbs")
    print(weight / 0.45)
elif typy.lower() == 'L' :
    print("Weight in Kg")
    print(weight * 0.45)
else:
    print("Enter correct weight")
print("END")
```
![image](https://user-images.githubusercontent.com/112848881/188485553-96f6d331-d011-4b5c-91a0-ce6dcdf2a366.png)
# While loops
While loops save us from writing code multiple times
```python
i = 1
while i <=5:
    print(i*'*')
    i = i + 1
```
![image](https://user-images.githubusercontent.com/112848881/188487210-bb78e5e7-002f-44ca-ae19-16fbc01b6079.png)
# Lists:
. list of objects
. list of names
. list of numbers
```python
shareholders = ["Saad", "Hamza", "Abu Bakkar", "Esha"]
shareholders[2] = "AbuBakar"
print(shareholders[0])
print(shareholders)
print(shareholders[0:3])
```
![image](https://user-images.githubusercontent.com/112848881/188488972-6cfeff65-955c-4b70-9ec4-2b4b08a5998c.png)
# List Methods:
Since Lists are also objects, they also have functionalities similar to the ones possessed by strings
```python
numbers = [1,2,3,4,5]
numbers.append(6)
print(numbers)
numbers.insert(0,-1)
print(numbers)
print(1 in numbers)
numbers.remove(4)
print(numbers)
numbers.clear()
print(numbers)
```
![image](https://user-images.githubusercontent.com/112848881/188490041-11a27922-9f49-465f-b64b-7fd44d9389fd.png)
# For Loops
```python
numbers = [1,2,3,4,5,6,7]
for item in  numbers:
    print(item)

    i=0
    while i < len(numbers):
        print(numbers[i])
        i = i + 1
```
# Range function
```python
numbers = range(5)
for number in numbers:
    print(number)
```
![image](https://user-images.githubusercontent.com/112848881/188495397-6e910e6e-5a57-4236-8afe-cca070bfb5f7.png)
# Tuples:
Tuples are like lists used to store sequence of objects but kind of like immutable i.e they cannot be changed
```python
numbers = (1,2,3)
numbers.count(3)
numbers.index(2)
```
END
