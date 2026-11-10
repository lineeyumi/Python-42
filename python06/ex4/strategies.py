import abc
from ex3.creatures import Creature, TransformCapability


class InvalidStrategyException(Exception):
    pass


class BattleStrategy(abc.ABC):
    @abc.abstractmethod
    def act(self, entity: Creature) -> None:
        pass

    @abc.abstractmethod
    def is_valid(self, entity: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, entity: Creature) -> bool:
        return True

    def act(self, entity: Creature) -> None:
        print(entity.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, entity: Creature) -> bool:
        return isinstance(entity, TransformCapability)

    def act(self, entity: Creature) -> None:
        if not self.is_valid(entity):
            raise InvalidStrategyException(
                f"Invalid Creature '{entity.name}' "
                "for this aggressive strategy"
            )
        if isinstance(entity, TransformCapability):
            print(entity.transform())
            print(entity.attack())
            print(entity.revert())
