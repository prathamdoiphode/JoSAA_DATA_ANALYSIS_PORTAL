from django.db import models
'''
from django.utils import timezone
from django.contrib.auth.models import User
'''

class jossaTable(models.Model):
    id = models.IntegerField(primary_key=True)
    Institute = models.CharField(max_length=100)
    Seat_Type = models.CharField(max_length=20)
    Gender = models.CharField(max_length=30)
    Opening_Rank = models.IntegerField()
    Closing_Rank = models.IntegerField()
    Year = models.IntegerField()
    Round_No = models.IntegerField()
    Programme = models.CharField(max_length=100)
    Duration_Yrs = models.IntegerField()
    Discipline = models.CharField(max_length=100)
    
    
    
    def __str__(self):
        return self.Programme
