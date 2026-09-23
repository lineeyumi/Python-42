#!/usr/bin/env python3

class Plant():
    name: str
    height: float
    age: int

    def __init__(
        self,
        name: str,
        height: float,
        age: int
    ) -> None:
        self.name = name
        self.height = height
        self.age = age

    @staticmethod
    def older_than_year(to_check: int) -> bool:
        if to_check > 365:
            return True
        else:
            return False




class Flower(Plant):
    color: str
    is_blooming: bool

    def __init__(
        self,
        name,
        height,
        age,
        color,
        is_blooming
    ) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = is_blooming

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.is_blooming:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    trunk: int

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk: int
    ) -> None:
        super().__init__(name, height, age)
        self.trunk = trunk

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk}")
        print(f"[asking the {self.name} to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of {self.height:.1f}cm "
            f"and {self.trunk:.1f}cm wide"
        )


class Vegetable(Plant):
    harvest: str
    nutri_value: int
    growth: int

    def __init__(
        self,
        name: str,
        height: float,
        age:int,
        harvest: str,
        nutri_value: int,
        growth: int
    ) -> None:
        super().__init__(name, height, age)
        self.harvest = harvest
        self.nutri_value = nutri_value
        self.growth = growth

    def veg_growth(self) -> None:
        new_age = self.age + self.growth
        new_height = self.height + self.height * 8 + 2
        self.age = new_age
        self.height = new_height

    def value(self) -> None:
        if self.age < 20:
            print(f" Nutritional Value: 0")
        else:
            print(f" Nutritional Value: {self.nutri_value}")

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest}")
        self.value()
        self.veg_growth()
        print(f"[make {self.name} grow and age for {self.growth} days]")
        super().show()
        print(f" Harvest season: {self.harvest}")
        self.value() 


class Anonymous(Plant): 



if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    days = 30
    print(f"Is {days} days more than a year? -> {Plant.older_than_year(days)}")
    days = 450
    print(f"Is {days} days more than a year? -> {Plant.older_than_year(days)}")
    print()
    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    print("[asking the rose to grow and bloom]")
    rose.bloom()
    rose.show()
    
    print()
    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    
    print()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 7, 10, "April", 20, 20)
    tomato.show()