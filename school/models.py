from django.db import models
CITY_CHOICE = (
    ("PUR","PURNEA"),
    ("PAT","PATNA"),
    ("BHOPAL","BHOPAL"),
    ("RANCHI","RANCHI"),
)
class Student(models.Model):
    name = models.CharField(max_length=200)
    fathers_name = models.CharField(max_length=200)
    contact = models.IntegerField()
    city = models.CharField(max_length=200,choices= CITY_CHOICE)
    state = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name

# Create your models here.
