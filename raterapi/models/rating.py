from django.db import models

# A game is rated, a player rates the game, given a score
class Rating(models.Model):
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="ratings")
    player_id = models.ForeignKey("Player", on_delete=models.CASCADE, related_name="ratings")
    rate_score = models.IntegerField()