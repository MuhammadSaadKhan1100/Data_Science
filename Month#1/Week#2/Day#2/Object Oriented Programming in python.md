# Object Oriented Programming: 🕸🧱📜
Object Oriented Programming(OOP) is a real world programming which involves two main aspects i.e
. Classes
. Objects
# Use:
It is used to represent complex data in our codes.
Some other ways inorder to represent data
. Jason
. XML
# Examples of classes:
classes are structure with attributes likewise
Customer class with two attributes
. name
. membership type
Now this membership type can have two objects
. Calub Golb
. Bread Bronze
```python
class Customer:
    def __init__(self,name,membership):
        self.name = name
        self.membership = membership
        print(" Valued Customer: ")

c = Customer("Saad" , "(Gold)")
print(c.name,c.membership)

c2 = Customer("Esha" , "(Premium)")
print(c2.name,c2.membership)
```
# Another way of doing the same thing:
``` python
class Customer:
    def __init__(self,name,membership):
        self.name = name
        self.membership = membership
        #print(" Valued Customer: ")

customer = [Customer("Saad","Gold"),Customer("Esha","Premium")]
print(customer[0].name, customer[0].membership)
```
# Custom Methods:
 . __init__() mthod:
Also known as initializer or constructor
Initializer is a method or section code whenever we create a new class in python
  # Example:
Customer()
__init__(self,anything extra e.g name,membership etc)
  # Difference between Parameters and Arguments
Parameters are variables attached to the method we are creating e.g name, membership are parameters while Argumets are values
assigned to the parameters e.g
Customer("Caleb","Gold") ,here Caleb and Gold are arguments assigned to membership
  # Note:
Parameters are definition while Arguments are invocation
. upgrade_membership(self new-membership)
e.g c.upgrade_membership("Bronze")
self.membership = new-membership
# Creating and Overriding methods:
```python
class Customer:
    def __init__(self,name,membership_type):
        self.name = name
        self.membership_type = membership_type

    def update_membership(self,new_membership):
        self.membership_type = new_membership

    def __str__(self):
        return self.name + " " + self.membership_type

    def print_all_customers(self):
        for customers in customer:
           print(customer)

    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return  True

        return  False
customer = Customer("Saad","Gold"), Customer("Esha","Luxury")
print(customer[0].membership_type,customer[1].membership_type)
customer[1].verified = True
print(customer[1].verified)  # Verification task
print(customer[1].membership_type) # old type of membership
customer[1].update_membership("Diamond")  # new type of membership mantained
print(customer[1].membership_type) # display of new membership
print(customer[0] == customer[1])  # checking if first customer and second customer's attribute is same or not
```
# Output:
![image](https://user-images.githubusercontent.com/112848881/188953334-0b73ea32-3aac-4afc-b83c-5bae261950eb.png)
# 3 Principles of OOP: 📚
. Encapsulation
. Inheritance
. Polymorphism
# Encapsulation:
Hiding the inner details of class or certain data and we only need to expose what is neeeded for user of class to use that class
Methods to get access of data:
. getter
. setter
Specific way to do Encapsulation in python is Property
We can add in the property and nothing is changed.
# Inheritance:
Allows to provide certain attributes to objects from base class
e.g User base class has two derived classes
. Customer
. Teacher
# Polymorphism:
. Kind of just extra step of inheritance where we can treat customers and teachers as same thing if we approach them as Users.
. Ability to create code that works with general users but is fully functional when you pass somethinng more specific e.g a teacher or a customer
```python
class User:
    def log(self):
        print(self)

class Teacher(User):
    def log(self):
        print("I m a teacher")

class Customer(User):
    def __init__(self,name,membership_type):
        self.name = name
        self.membership_type = membership_type

        @property
        def name(self):                       # Getter function
            print("Getting name")
            return self._name

        @name.setter
        def name(self,name):                  # Setter function
            print("Setting name")
            self._name = name

    def update_membership(self,new_membership):
        self.membership_type = new_membership

    def __str__(self):
        return self.name + " " + self.membership_type

    def print_all_customers(self):
        for customers in customer:
           print(customer)

    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return  True

        return  False

    __hash__ = None
    __repr__ = __str__
users = [Customer("Saad","Gold"), Customer("Esha","Luxury"), Teacher()]
for user in users:
    user.log()
```
🔚
