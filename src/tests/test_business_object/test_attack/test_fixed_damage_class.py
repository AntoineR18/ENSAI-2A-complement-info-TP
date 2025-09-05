from business_object.attack.fixed_damage_attack import FixedDamageAttack
from business_object.pokemon.attacker_pokemon import AttackerPokemon

class TestFixedDamageAttack:
    def test_fixed_damage_attack_returns_power_every_time(self):
        heatran = AttackerPokemon(level=100)
        caterpie = AttackerPokemon(level=1)

        flamethrower = FixedDamageAttack(
            power=100,
            name="Flamethrower",
            description="The pokemon blows fire onto its poor opponent."
            )
        damage_dealt_by_flamethrower = flamethrower.compute_damage(heatran, caterpie)

        tackle = FixedDamageAttack(
            power=1,
            name="Tackle",
            description="The pokemon hurls itself at the defending pokemon."
        )
        damage_dealt_by_tackle = tackle.compute_damage(caterpie, heatran)
        
        assert damage_dealt_by_flamethrower == 100
        assert damage_dealt_by_tackle == 1

if __name__ == "__main__":
    import pytest

    pytest.main([__file__])