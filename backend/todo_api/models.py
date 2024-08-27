from django.db import models

# Create your models here.
class Todos(models.Model):
    header = models.CharField(max_length=200)
    contains = models.CharField(max_length=1000)
    
    def __str__(self) -> str:
        return self.header