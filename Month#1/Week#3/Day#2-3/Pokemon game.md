# Pokemon world game using OOP Concept
![image](https://user-images.githubusercontent.com/112848881/190215100-a923f149-dd68-41fa-b367-c1c2de2405c6.png)
* Code: 💻
```python
print("-------Welcome to Pokemon World Battle Game 🐢🍀🔥--------")
print("                   1-1 Battle                 ")
class Pokemon:
    def __init__(self,name,type,max_hp):
        self.name = name
        self.type = type
        self.max_hp = max_hp
        self.hp = max_hp

    @staticmethod
    def typewheel(type1,type2):
        result = {0 : 'win', 1 : 'lose', -1 : 'tie'}

        Poke_Types = {'grass':1,'fire':0, 'water':2}

        wl_Matrix = [
            [-1,0,1], #grass
            [1,-1,0], #fire
            [0,1,-1] #water
        ]
        wl_result = wl_Matrix[Poke_Types[type1]][Poke_Types[type2]]
        return result[wl_result]

    def __str__(self):
        return f'name:{self.name = },({self.type}:{self.hp}/{self.max_hp})'

    def feed(self):
        if self.hp < self.max_hp:
            self.hp += 1
            print(f'{self.name} is recovered')
        else:
            print(f'{self.name} is full.')

    def battle(self,other):
        wl_result = self.typewheel(self.type,other.type)
        print(f'Battle between {self.name,other.name}')
        if wl_result == 'lose':
            self.hp = 0
            print(f"\n{self.name} fainted!\n")
        elif wl_result == 'tie':
            self.hp -= 10
            other.hp -= 10
            print(f"\n{self.name} and {other.name} battled hard. It's a tie.\n")
        elif wl_result == 'win':
            other.hp = 0
            print(f"\n{self.name} won. Congratulations!\n")


if __name__ == "__main__":
    bulb = Pokemon("Bulbasaur",'grass',100)
    charm = Pokemon("Charmander","fire",150)
    squirt = Pokemon("Squirtle","water",110)
   # print(bulb,charm)
    print(bulb.name)
    print(charm.name)
    print(squirt.name)
    print(f'Match-1 \n {bulb.battle(charm)}')
    print(f'Match-2 \n {charm.battle(squirt)}')
    print(f'Match-3 \n {squirt.battle(squirt)}')
```
* OUTPUT:
* ![image](https://user-images.githubusercontent.com/112848881/190216819-28e8fb6f-305f-4b8b-b078-8163b9238bfa.png)

* 🔚
