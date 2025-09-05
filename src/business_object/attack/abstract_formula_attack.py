from .abstract_attack.py import AbstractAttack
from abc import abstractmethod


class AbstractFormulaAttack(AbstractAttack):
    @abstractmethod
    def get_attack_stat(self, attacking_pokemon) -> float:
        pass

    @abstractmethod
    def get_defense_stat(self, defending_pokemon) -> float:
        pass

    def compute_damage(self, attacking_pokemon, defending_pokemon) -> int: 
        return self.power
