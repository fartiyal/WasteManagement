from django.db import models

class WorkerDetails(models.Model):
    First_Name=models.CharField(max_length=40)
    Middle_Name=models.CharField(max_length=40)
    Last_Name=models.CharField(max_length=40)
    Mobile_Number=models.CharField(primary_key=True,max_length=14)
    Gender=models.CharField(max_length=10)
    Age=models.IntegerField()
    Address=models.CharField(max_length=200)
    Pin_Code=models.IntegerField()




# Create your models here.
