from business_object.pokemon.attacker_pokemon import AttackerPokemon
from business_object.statistic import Statistic

class TestAbsrtactPokemon:
    def test_level_up(self):
        garchomp = AttackerPokemon(stat_current=Statistic(speed=100, attack=100))
        jigglypuff = AttackerPokemon(stat_current=Statistic(speed=100, attack=100), level=8)

        garchomp.level_up()
        jigglypuff.level_up()
        jigglypuff.level_up()

        assert garchomp.level == 1
        assert jigglypuff.level == 10


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])