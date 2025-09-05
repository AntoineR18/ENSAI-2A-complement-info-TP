from abc import ABC, abstractmethod
from ..pokemon.abstract_pokemon import AbstractPokemon

class AbstractAttack(ABC):
    """
    Object representing an attack.
    Can compute damage depending on the attacking pokemon throwing the attack
    and the defending pokemon receving it.
    """

    # -------------------------------------------------------------------------
    # Constructor
    # -------------------------------------------------------------------------

    def __init__(self, power:int, name:str, description:str):
        # -----------------------------
        # Attributes
        # -----------------------------
        self._power: int = power
        self._name: str = name
        self._description: str = description
    
    # -------------------------------------------------------------------------
    # Methods
    # -------------------------------------------------------------------------

    @abstractmethod
    def compute_damage(
        self, attacking_pokemon:AbstractPokemon, defending_pokemon:AbstractPokemon
        ) -> int:
        pass

    # -------------------------------------------------------------------------
    # Setters and getters
    # -------------------------------------------------------------------------

    @property
    def power(self):
        return self._power

    @property
    def name(self):
        return self._name
    
    @property
    def description(self):
        return self._description
