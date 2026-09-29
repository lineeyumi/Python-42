#!/usr/bin/env python3

class Plant():
    name: str
    height: float
    plant_age: int

    class Stats:
        count_grow: int
        count_age: int
        count_show: int
        plant_name: str

        def __init__(self, plant_name: str) -> None:
            self.count_grow = 0
            self.count_age = 0
            self.count_show = 0
            self.plant_name = plant_name

        def display(self) -> None:
            print(f"[statistics for {self.plant_name}]")
            print(
                f"Stats: {self.count_grow} grow, "
                f"{self.count_age} age, "
                f"{self.count_show} show"
            )

    def __init__(
        self,
        name: str,
        height: float,
        plant_age: int
    ) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age
        self.stats = self.Stats(self.name)

    @staticmethod
    def older_than_year(to_check: int) -> bool:
        if to_check > 365:
            return True
        else:
            return False

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.plant_age} days old")
        self.stats.count_show += 1


class Flower(Plant):
    color: str
    is_blooming: bool

    def __init__(
        self,
        name: str,
        height: float,
        plant_age: int,
        color: str,
        is_blooming: bool
    ) -> None:
        super().__init__(name, height, plant_age)
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
    count_shade: int

    def __init__(
        self,
        name: str,
        height: float,
        plant_age: int,
        trunk: int
    ) -> None:
        super().__init__(name, height, plant_age)
        self.trunk = trunk
        self.count_shade = 0

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk:.1f} cm")

    def produce_shade(self) -> None:
        self.count_shade += 1
        print(f"[asking the {self.name} to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of {self.height:.1f}cm "
            f"and {self.trunk:.1f}cm wide"
        )

    def show_stats(self) -> None:
        self.stats.display()
        print(f"{self.count_shade} shade")


class Seed(Flower):
    seed: int

    def __init__(
        self,
        name: str,
        height: float,
        plant_age: int,
        color: str,
        is_blooming: bool
    ) -> None:
        super().__init__(name, height, plant_age, color, is_blooming)
        self.seed = 0

    def bloom(self) -> None:
        self.is_blooming = True
        self.seed = 42

    def show(self) -> None:
        super().show()
        if self.is_blooming:
            print(f" Seeds: {self.seed}")
        else:
            print(" Seeds: 0")

    def grow(self) -> None:
        self.height += 30
        self.stats.count_grow += 1

    def age(self) -> None:
        self.plant_age += 20
        self.stats.count_age += 1


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
    rose.stats.display()
    print("[asking the rose to grow and bloom]")
    rose.bloom()
    rose.grow()
    rose.show()
    rose.stats.display()
    print()
    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    oak.show_stats()
    oak.produce_shade()
    oak.show_stats()
    print()
    print("=== Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow", False)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    sunflower.stats.display()
    print()
    print("=== Anonymous")
    anonymous = Plant.anonymous()
    anonymous.show()
    anonymous.stats.display()
