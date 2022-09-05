# Introduction to Python:
Python is a very straightforward and user friendly Programming language. It has very simple syntax.
# Topic 1                           Hello, World!
For printing simple or for showing an output via python a programmer is required to write print then ( " then you enter your text in here " )
# Example:
print("Hello, Electrical Engineer Saad!")
# Indentation:
Python uses indentation for blocks usually through tabs and spaces instead of curly braces like in C and C++ 
```python
x = 10
if x == 10:
    print("Value of x is 10")
```
 
# Topic 2                    Variables and Types
Python supports two types of numbers
1) Integers ( mostly known as int).
2) Floating point.

# Strings
Strings are defined either with a single quote or a double quote. You " Your Text here" Everything which is inside the single or double quote is considered a string.
You can apply mathematical operators like + and x on strings.

# Exercise Example:
The target of this exercise is to create a string, an integer, and a floating point number. The string should be named mystring and should contain the word "hello". The floating point number should be named myfloat and should contain the number 10.0, and the integer should be named myint and should contain the number 20.
 ```python
 Mystring = "hello"
myfloat = 10.0
myint = 20
print(Mystring)
print(myfloat)
print(myint)
 ```
 
# Topic 3          Lists
Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish. Lists can also be iterated over in a very simple manner.

. append()	Adds an element at the end of the list
. clear()	Removes all the elements from the list
. copy()	Returns a copy of the list
. count()	Returns the number of elements with the specified value
. extend()	Add the elements of a list (or any iterable), to the end of the current list
. index()	Returns the index of the first element with the specified value
. insert()	Adds an element at the specified position
. pop()	Removes the element at the specified position
. remove()	Removes the first item with the specified value
. reverse()	Reverses the order of the list
. sort()	Sorts the list.
# Exercise Example:
In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method. You must add the numbers 1,2, and 3 to the "numbers" list, and the words 'hello' and 'world' to the strings variable.

You will also have to fill in the variable second_name with the second name in the names list, using the brackets operator []. Note that the index is zero-based, so if you want to access the second item in the list, its index will be 1.
 
 ```python
 number = []
strings = []
number.append(1)
number.append(2)
number.append(3)
strings.append("hello")
strings.append("world")
second_name = number[1]
print(number[0])
print(number[1])
print(number[2])
print(strings[0] + strings[1])
print(second_name)

 ```
