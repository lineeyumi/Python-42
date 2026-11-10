import abc


class Creature(abc.ABC):
    def __init__(self, name: str, creature_type: str) -> None:
        self.name: str = name
        self.creature_type: str = creature_type

    @abc.abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.creature_type} type Creature"


class Flameling(Creature):
    def __init__(self, name: str = "Flameling") -> None:
        super().__init__(name, "Fire")

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self, name: str = "Pyrodon") -> None:
        super().__init__(name, "Fire/Flying")

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class TransformCapability(abc.ABC):
    def __init__(self) -> None:
        self._is_transformed: bool = False

    @abc.abstractmethod
    def transform(self) -> str:
        pass

    @abc.abstractmethod
    def revert(self) -> str:
        pass


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str = "Shiftling") -> None:
        Creature.__init__(self, name, "Normal")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self._is_transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self._is_transformed = False
        return f"{self.name} returns to normal."

    def attack(self) -> str:
        if self._is_transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str = "Morphagon") -> None:
        Creature.__init__(self, name, "Normal/Dragon")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self._is_transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._is_transformed = False
        return f"{self.name} stabilizes its form."

    def attack(self) -> str:
        if self._is_transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."
