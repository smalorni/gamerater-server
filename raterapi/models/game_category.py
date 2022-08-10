from django.db import models

# The class joins/bridges Game tables and Category Tables, acts as middleman
class GameCategory(models.Model):
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE)
    category_id = models.ForeignKey("Category", on_delete=models.CASCADE)