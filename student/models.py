from django.db import models
from adminmodule.models import Course,Batch
from datetime import date

# Create your models here.
class Student(models.Model):
    sname = models.CharField(max_length=50)
    semail = models.CharField(max_length=50)
    smobile= models.BigIntegerField()
    password = models.CharField(max_length=50,default='12345')
    img = models.ImageField(upload_to="userimage/",default="userimage/userprofile.jpg")
    status = models.CharField(max_length=10,default="Inactive")
    course = models.ManyToManyField(Course,blank=True)
    batch = models.ManyToManyField(Batch,blank=True)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.sname

class User_Otp(models.Model):
     user_email = models.CharField(max_length=50,blank=True)
     time_st=models.DateTimeField(auto_now=True, auto_now_add=False)
     otp=models.SmallIntegerField()
    #  def __str__(self):
    #     return self.otp
