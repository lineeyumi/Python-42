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

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


class Flower(Plant):
    color: str
    is_blooming: bool

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str
    ) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

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

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of {self.height:.1f}cm "
            f"and {self.trunk:.1f}cm wide"
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk}")


class Vegetable(Plant):
    harvest_season: str
    nutritional_value: int

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest
        self.nutritional_value = 0

    def grow(self) -> None:
        self.height += 2.1
        self.nutritional_value += 1

    def day_age(self) -> None:
        self.age += 1

    def old(self, days: int) -> None:
        count = 0
        while count < days:
            self.day_age()
            self.grow()
            count += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    oak.produce_shade()
    print()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10, "April")
    tomato.show()
    days = 20
    print(f"[make tomato grow and age for {days} days]")
    tomato.old(days)
    tomato.show()
