from abc import abstractmethod, ABC
from enum import Enum
import yaml
import random


class EntityType(Enum):
    BARBARIAN = 0
    ELF = 1
    WIZARD = 2
    DRAGON = 3
    KNIGHT = 4


class Entity(ABC):
    def __init__(self, name: str, entity_type: EntityType, speed: int, power: int, special_power: int,
                 health: int = 100):
        self.name = name
        self.type = entity_type
        self.health = health
        self.speed = speed
        self.power = power
        self.special_power = special_power

    def __repr__(self):
        return f"<{self.name} ({self.type.name}) health={self.health}, power={self.power}, special_power={self.special_power}, speed={self.speed}>"

    @abstractmethod
    def special_attack(self):
        pass

    @abstractmethod
    def attack(self):
        pass


class Barbarian(Entity):
    def special_attack(self):
        pass

    def attack(self):
        pass

    def __init__(self):
        super().__init__(self.generate_name(), EntityType.BARBARIAN, 50, 70, 20)

    @staticmethod
    def generate_name() -> str:
        with open("assets/name_syllables.yml", "r") as stream:
            name_syllables = yaml.safe_load(stream)
        return "".join(random.sample(name_syllables["syllables"][EntityType.BARBARIAN.value], 3))


class Elf(Entity):

    def special_attack(self):
        pass

    def attack(self):
        pass

    def __init__(self):
        super().__init__(self.generate_name(), EntityType.ELF, 10, 30, 60)

    @staticmethod
    def generate_name() -> str:
        with open("assets/name_syllables.yml", "r") as stream:
            name_syllables = yaml.safe_load(stream)
        return "-".join(random.sample(name_syllables["syllables"][EntityType.ELF.value], 3))


class Wizard(Entity):

    def special_attack(self):
        pass

    def attack(self):
        pass

    def __init__(self):
        super().__init__(self.generate_name(), EntityType.WIZARD, 30, 50, 70)

    @staticmethod
    def generate_name() -> str:
        with open("assets/name_syllables.yml", "r") as stream:
            name_syllables = yaml.safe_load(stream)
        return "-".join(random.sample(name_syllables["syllables"][EntityType.WIZARD.value], 3))


class Dragon(Entity):

    def special_attack(self):
        pass

    def attack(self):
        pass

    def __init__(self):
        super().__init__(self.generate_name(), EntityType.DRAGON, 50, 90, 40)

    @staticmethod
    def generate_name() -> str:
        with open("assets/name_syllables.yml", "r") as stream:
            name_syllables = yaml.safe_load(stream)
        return "-".join(random.sample(name_syllables["syllables"][EntityType.DRAGON.value], 3))


class Knight(Entity):

    def special_attack(self):
        pass

    def attack(self):
        pass

    def __init__(self):
        super().__init__(self.generate_name(), EntityType.KNIGHT, 60, 60, 10)

    @staticmethod
    def generate_name() -> str:
        with open("assets/name_syllables.yml", "r") as stream:
            name_syllables = yaml.safe_load(stream)
        return "".join(random.sample(name_syllables["syllables"][EntityType.KNIGHT.value], 2))
