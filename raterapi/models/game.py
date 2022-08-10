from django.db import models

# Who plays the game, what is name of game, what is game about, who designed game
# What year was game released, how many players can play game
# How long is game, what ages can play
class Game(models.Model):
    player = models.ForeignKey("Player", on_delete=models.CASCADE, related_name="games",)
    title = models.CharField(max_length=100)
    description = models.TextField
    designer = models.CharField(max_length=100)
    year_released = models.CharField(max_length=50)
    number_of_players = models.IntegerField()
    estimated_time_to_play = models.IntegerField()
    age_recommendation = models.IntegerField()