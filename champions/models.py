from django.db import models


# Create your models here.
class Champion(models.Model):
    name = models.CharField(max_length=100)
    health_points = models.DecimalField(max_digits=10, decimal_places=5)
    health_points_per_level = models.DecimalField(max_digits=10, decimal_places=5)
    health_regeneration = models.DecimalField(max_digits=10, decimal_places=5)
    health_regeneration_per_level = models.DecimalField(max_digits=10, decimal_places=5)
    mana = models.DecimalField(max_digits=10, decimal_places=5)
    mana_per_level = models.DecimalField(max_digits=10, decimal_places=5)
    mana_regeneration = models.DecimalField(max_digits=10, decimal_places=5)
    mana_regeneration_per_level = models.DecimalField(max_digits=10, decimal_places=5)
    atack_damage = models.DecimalField(max_digits=10, decimal_places=5)
    atack_damage_per_level = models.DecimalField(max_digits=10, decimal_places=5)
    atack_speed = models.DecimalField(max_digits=10, decimal_places=5)
    atack_speed_per_level = models.CharField(max_length=10)
    armor = models.DecimalField(max_digits=10, decimal_places=5)
    armor_per_level = models.DecimalField(max_digits=10, decimal_places=5)
    magic_resistance = models.DecimalField(max_digits=10, decimal_places=5)
    magic_resistance_per_level = models.DecimalField(max_digits=10, decimal_places=5)
    movement_speed = models.DecimalField(max_digits=20, decimal_places=5)
    atack_range = models.DecimalField(max_digits=20, decimal_places=5)
