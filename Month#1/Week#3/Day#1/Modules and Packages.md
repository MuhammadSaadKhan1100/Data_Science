# Modules: 📦
* Modules are a logical section of code
* Modules are of type .py
* Modules contains tons of lines of code
* They make it easier to handle complex codes
# Syntax of Module: 📏
from python_file import class of that file
# Packages: 🎁
* Packages are a collection of modules
* Example:
* Importing random modules from pre-default math directory

# classes.py
```python
from calc import  Car
class Electric_car:
    def __init__(self,company_name,colour,horse_power,max_speed):
        self.company_name = company_name
        self.colour = colour
        self.horse_power = horse_power
        self.max_speed = max_speed

    def toyota(self):
        return f'{self.company_name} has started manufacturing Electric vehicles'

    def spin(max_speed = '230 miles per hour'):
        return f'The car moves with high speed of 230'


specs = Electric_car('Toyota','black','660','200')
spec2 = Car()
print(specs.toyota())
print(specs.spin())
# print(spec2.car_area('2','1'))
d = Car.car_area(2,1)
print("Area aquired by car: ",d)
f = Car.car_volume(2,1,7)
print("Volume aquired by car: ",f)
```
# calc.py
```python
class Car:

    def car_area(a1,a2):
        area = a1 * a2
        return area

    def car_volume(a1,a2,a3):
        volume = a1 * a2 * a3
        return volume
```
Output:
![image](https://user-images.githubusercontent.com/112848881/189730833-31c7ef2b-5549-4672-b831-482b6920ec95.png)
* 🔚
