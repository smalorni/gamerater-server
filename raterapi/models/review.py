from django.db import models

# A review is associated with a game, a player writes the review which is a description about the game
class Review(models.Model): 
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="reviews")
    player_id = models.ForeignKey("Player", on_delete=models.CASCADE, related_name="reviews")
    description = models.TextField()