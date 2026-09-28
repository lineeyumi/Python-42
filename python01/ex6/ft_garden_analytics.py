#!/usr/bin/env python3

class Plant():
    name: str
    height: float
    age: int

    class Stats:
        count_grow: int
        count_age: int
        count_show: int
        plant_name: str

        def __init__(
            self,
            plant_name: str
            ) -> None:
            self.count_grow = 0
            self.count_age = 0
            self.count_show = 0
            self.plant_name = plant_name

        def display(self) -> None:
            print(f"[statistics for {self.plant_name}]")

    def __init__(
        self,
        name: str,
        height: float,
        age: int
    ) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.stats = self.Stats(self.name)

    @staticmethod
    def older_than_year(to_check: int) -> bool:
        if to_check > 365:
            return True
        else:
            return False

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    def show(self):
        print(
            f"Stats: {self.count_grow} grow, {self.count_age} age, "
            f"{self.count_show} show"
            )
        self.stats.count_show += 1


class Flower(Plant):
    color: str
    is_blooming: bool

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        is_blooming: bool
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

    def grow(self) -> None:
        self.height += 8
        self.stats.count_grow += 1


class Tree(Plant):
    trunk: int
    shade: int

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk: int
    ) -> None:
        super().__init__(name, height, age)
        self.trunk = trunk
        self.shade = 0

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk}")
        print(f"[asking the {self.name} to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of {self.height:.1f}cm "
            f"and {self.trunk:.1f}cm wide"
        )

    def has_shade(self) -> None:
        print(f"{self.shade} shade")
        self.shade += 1


class Seed(Flower):
    seed: int

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        seed: int,
        is_blooming: bool
    ) -> None:
        super().__init__(name, height, age, color, is_blooming)
        self.seed = seed

    def bloom(self):
        self.is_blooming = True

    def show(self):
        super().show()
        if self.is_blooming:
            print(f" Seeds: {self.seed}")
        else:
            print(" Seeds: 0")


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    days = 30
    print(f"Is {days} days more than a year? -> {Plant.older_than_year(days)}")
    days = 450
    print(f"Is {days} days more than a year? -> {Plant.older_than_year(days)}")
    print()
    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red", False)
    rose.show()

    print("[asking the rose to grow and bloom]")
    rose.bloom()
    rose.show()

    print()
    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()

    print()
    print("=== Seed")
    sunflower = Seed("sunflower", 7, 10, "yellow", 42, False)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.show()
