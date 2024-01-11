# Here are models that i can use in my database

from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=255, blank=True)
    surname = models.CharField(max_length=255, blank=True)
    pesel = models.PositiveIntegerField(unique=True)
    MALE = 'Male'
    FEMALE = 'Female'
    N = 'Not selected'
    GENDER_CHOICES = [(MALE, 'Male'), (FEMALE, 'Female'), (N, "I don't want to answer")]

    sex = models.CharField(
        max_length=12,
        choices=GENDER_CHOICES,
        default=N,
    )

    def __str__(self):
        return f"{self.name} {self.surname} {self.pesel} {self.sex}"


class Hotel(models.Model):
    room = models.ManyToManyField(Person, blank=True)
    max_persons = models.PositiveIntegerField(default=2)
