
from django.db import models

# Create your models here.

class Profile(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.fname
    


