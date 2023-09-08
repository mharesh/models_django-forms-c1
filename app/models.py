from django.db import models

# Create your models here.

class Student(models.Model):
    Sname = models.CharField(max_length=123)
    Sid = models.IntegerField()
    Semail = models.EmailField()

    def __str__(self):
        return self.Sname
    