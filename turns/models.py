from django.db import models

# Create your models here.
class Turn(models.Model):
    """
    Description: Model Description
    """
    room = models.ForeignKey('rooms.Room', on_delete=models.CASCADE,related_name='turns')
    player_name = models.CharField(max_length=200)
    card_value = models.CharField(max_length=100)
    card_position = models.IntegerField()
    

    class Meta:
        pass