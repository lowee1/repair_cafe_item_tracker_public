from django.db import models

# Create your models here.
class Item(models.Model):
    item = models.TextField()
    problem = models.TextField()
    owner = models.TextField()
    owner_email = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.TextField(default="Unassigned")
    assigned_to = models.TextField(default="Unassigned")
    difficulty = models.IntegerField(default=0)
    image = models.TextField(blank=True)
    hurry_count = models.IntegerField(default=0)
