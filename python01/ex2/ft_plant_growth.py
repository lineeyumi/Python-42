#!/usr/bin/env python3

class Plant:
    name: str
    height: float
    age_days: int

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age_days} days old")

    def age(self) -> None:
        self.age_days = self.age_days + 1

    def grow(self) -> None:
        self.height = self.height + 0.8


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25
    rose.age_days = 30
    rose.show()
    height_start = rose.height
    day = 1
    while (day >= 1 and day <= 7):
        print(f"=== Day {day} ===")
        rose.age()
        rose.grow()
        rose.show()
        day = day + 1
    print(f"Growth this week: {rose.height - height_start:.1f}cm")
