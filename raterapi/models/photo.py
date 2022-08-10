from django.db import models

# A game is associated with a photo, the player uploads the photo, photo contains a url
class Photo(models.Model):
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="photos")
    player_id = models.ForeignKey("Player", on_delete=models.CASCADE, related_name="photos")
    url = models.CharField(max_length=250)