from django.db import models

# Create your models here.
class Room(models.Model):
    """
    Description: Model Description
    """
    name = models.CharField(max_length=200)
    number_of_players = models.IntegerField()
    result = models.CharField(max_length=300,null=True,blank=True)
    create_date = models.DateTimeField(auto_now=True) 

    class Meta:
    	"""docstring for Meta"""
    	ordering = ('-create_date',)
    		
