class Spectator:
    def __init__(self, id:int, age:int, money:float) -> None:
        self.id = id
        self.age = age
        self.money = money

    def __str__(self):
        return f'id {self.id}, age {self.age}, money {self.money}'
    
    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.id == other.id and self.age == other.age and self.money == other.money