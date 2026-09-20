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

    def show(self):
        print(f"=== {self.__class__.__name__}")
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

    class Flower(Plant):
        def __init__(
            self,
            name: str,
            height: float,
            age: int,
            color: str
        ) -> None:
            super().__init__(name, height, age)

        def bloom(self) -> None:
            bloom_flower: str
            

if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rose = Plant("Rose", 15, 10, "Flower")
    oak = Plant("Oak", 15, 10, "Tree")
    tomato = Plant("Tomato", 15, 10, "Vegetable")