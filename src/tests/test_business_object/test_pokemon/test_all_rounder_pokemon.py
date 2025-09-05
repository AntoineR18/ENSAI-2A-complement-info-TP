from business_object.pokemon.all_rounder_pokemon import AllRounderPokemon
from business_object.statistic import Statistic


class TestAllRounderPokemon:
    def test_get_coef_damage_type(self):
        snorlax = AllRounderPokemon(stat_current=Statistic(sp_atk=100, sp_def=100))

        multiplier = snorlax.get_pokemon_attack_coef()

        assert multiplier == 2


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])