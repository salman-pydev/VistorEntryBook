from django.db import models

class UserDetail(models.Model):
    userName = models.CharField(max_length=50)
    Email = models.EmailField(primary_key=True)
    pw = models.CharField(max_length=20)

class VisitorDeatils(models.Model):
    UserName = models.CharField(max_length=50)
    Cname = models.CharField(max_length=50)
    Email = models.EmailField()
    ContactNo = models.IntegerField()
    Date = models.DateField()
    Address = models.CharField(max_length=500)
    City = models.CharField(max_length=20)
    State = models.CharField(max_length=30)
    note = models.CharField(max_length=500)