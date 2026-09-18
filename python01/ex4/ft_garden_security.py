#!/usr/bin/env python3

class Plant:
    _name: str
    _height: float
    _age: int

    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._height = height
        self._age = age

    def get_name(self) -> str:
        return self._name

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height}cm")

    def get_height(self) -> float:
        return self._height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age
            print(f"Age updated: {self._age} days")

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    print(
        f"Plant created: {rose.get_name()}: "
        f"{rose.get_height():.1f}cm, "
        f"{rose.get_age()} days old"
    )
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-10)
    rose.set_age(-15)
    print()
    print("Current state: ", end="")
    rose.show()
