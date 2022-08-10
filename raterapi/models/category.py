import imp
from django.db import models

# What kind of category does game falls under
class Category(models.Model):

    label = models.CharField(max_length=50)