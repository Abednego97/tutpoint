from django.db import models

# Create your models here.

class register(models.Model):
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    whatsapp = models.CharField(max_length=400)
    number = models.CharField(max_length= 200)
    learn= models.CharField(max_length=400)

    def __str__(self):
        return self.name