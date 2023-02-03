from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS={
    ("new", "nowy"),
    ("during", "w trakcie"),
    ("finished", "zakończony")
}

class Item(models.Model):
    name = models.CharField(max_length=255, unique=True)
    shortDescription = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.TextField()
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    status = models.CharField(choices=STATUS, default="new", max_length=255)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    maxPrice = models.DecimalField(max_digits=10, decimal_places=0)
    voteDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


