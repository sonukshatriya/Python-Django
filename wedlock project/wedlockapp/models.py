from django.db import models
GENDER = (('male', "Male"), ('female', "Female"))
# Create your models here

class wedlock(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=10)
    profile_seeking_for = models.CharField(max_length=10)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, choices=GENDER)
    religion = models.CharField(max_length=10)
    mother_tongue = models.CharField(max_length=10)



