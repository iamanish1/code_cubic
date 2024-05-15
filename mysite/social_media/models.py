from django.db import models

# Create your models here.
class Reguser(models.Model):
    FirstName=models.TextField()
    LastName=models.TextField()
    Username=models.TextField()
    email=models.EmailField()
    catogery=models.TextField()
    password=models.TextField()

class Courses(models.Model):
    CourseId=models.IntegerField()
    CourseName=models.TextField()
    Language=models.TextField()
    Category=models.TextField()
    duration=models.TextField()
    CoursePrice=models.IntegerField()

class projects(models.Model):
    ProjectId=models.IntegerField()
    ProjectTitle=models.TextField()
    ProjectCategory=models.TextField()
    ProjectDura=models.IntegerField()
    ProjectDec=models.TextField()

class Internship(models.Model):
    InternId=models.IntegerField()
    InternTitle=models.TextField()
    InternCategory=models.TextField()
    InternDur=models.TextField()
    INternCompamy=models.TextField()

class Community(models.Model):
    Comments=models.TextField()
    Like=models.IntegerField()
    share=models.IntegerField()
    Save=models.IntegerField()
  


