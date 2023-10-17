from django.db import models

# Create your models here.
class ttwenty_team(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    talent = models.CharField(max_length=25)
    score = models.IntegerField()
    
    
class test_match(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    talent = models.CharField(max_length=25)
    score = models.IntegerField()    