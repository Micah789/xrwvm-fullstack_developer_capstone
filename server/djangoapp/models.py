# Uncomment the following imports before adding the Model code

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    '''
    CarMake model

    Attributes:
    name: CharField
    description: TextField
    color: CharField

    Methods:
    __str__: returns the name of the car make
    '''
    name = models.CharField(max_length=100)
    description = models.TextField()
    COLORS = [
        ('RED', 'Red'),
        ('BLUE', 'Blue'),
        ('WHITE', 'White'),
        ('BLACK', 'Black')
    ]
    color = models.CharField(max_length=20, choices=COLORS)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    '''
    CarModel model

    Attributes:
    car_make: ForeignKey
    name: CharField
    type: CharField
    year: IntegerField
    seats: IntegerField

    Methods:
    __str__: returns the name of the car model
    '''
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2023, validators=[
        MaxValueValidator(2023),
        MinValueValidator(2015)
    ])

    seats = models.IntegerField(default=5, validators=[
        MaxValueValidator(7),
        MinValueValidator(3)
    ])

    def __str__(self):
        return self.name
