from django.db import models

# Create your models here.
class Team(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        
class Player(models.Model):
    player_name = models.CharField(max_length=150)
    jersey_number = models.IntegerField(default=0)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players")
    
    def __str__(self):
        return self.player_name