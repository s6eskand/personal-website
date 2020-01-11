from django.db import models


# Create your models here.
class Contact(models.Model):
    user_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.user_name
