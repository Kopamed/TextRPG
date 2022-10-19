from abc import abstractmethod, ABC
from enum import Enum


class EntityType(Enum):
    BARBARIAN = 0
    ELF = 1
    WIZARD = 2
    DRAGON = 3
    KNIGHT = 4


class Entity(ABC):
    def __init__(self, name: str, entity_type: EntityType, speed: int, attack: int, special_attack: int,
                 health: int = 100):
        self.name = name
        self.type = entity_type
        self.health = health
        self.speed = speed
        self.attack = attack
        self.special_attack = special_attack

    @abstractmethod
    def special_power(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    @classmethod
    def generate_name(cls, entity_type: EntityType) -> str:
        return ""

    @classmethod
    def from_entity_type(cls, entity_type: EntityType):
        if entity_type == EntityType.BARBARIAN:
            return cls(cls.generate_name(entity_type), entity_type, 50, 70, 20)


