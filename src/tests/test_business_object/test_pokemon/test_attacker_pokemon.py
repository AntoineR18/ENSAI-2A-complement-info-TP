from business_object.pokemon.attacker_pokemon import AttackerPokemon
from business_object.statistic import Statistic


class TestAttackerPokemon:
    def test_get_coef_damage_type(self):
        garchomp = AttackerPokemon(stat_current=Statistic(speed=100, attack=100))
        pikachu = AttackerPokemon(stat_current=Statistic(speed=500))

        garchomp_multiplier = garchomp.get_pokemon_attack_coef()
        pikachu_multiplier = pikachu.get_pokemon_attack_coef()

        assert garchomp_multiplier == 2
        assert pikachu_multiplier == 3.5


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])