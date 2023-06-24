from django.db import models

# Create your models here.
class Game(models.Model):

    game_name=models.CharField(max_length=30,primary_key=True)
  
    def __str__(self) -> str:
        return self.game_name
class Cup(models.Model):
    no=models.IntegerField()
    game_name=models.ForeignKey(Game,max_length=30,on_delete=models.CASCADE)
    cup_name=models.CharField(max_length=100)
