from django.db import models

# Create your models here.

GendersOption=(
    ('M','Male'),
    ('F','Female')
)

class Student(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, blank=False)
    Contact_Number=models.CharField(max_length=15, blank=True)
    Gender=models.CharField(max_length=1,blank=True,choices=GendersOption)

    def __str__(self):
        return "{0} {1} {2} {3}".format(
            self.name,
            self.email,
            self.Contact_Number,
            self.Gender
        )