from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create a Car Make model
class CarMake(models.Model):
    '''
    Name
    Description
    Any other fields
    __str__ method to print a car make object
    '''
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Other fields as needed

    def __str__(self):
        return self.name  # Return the name as the string representation


# Create a Car Model model `class CarModel(models.Model):
class CarModel(models.Model):
    '''
    Many-To-One relationship to Car Make model (One Car Make has many
    Car Models, using ForeignKey field)
    Name
    Type (CharField with a choices argument to provide limited choices
    such as Sedan, SUV, WAGON, etc.)
    Year (IntegerField) with min value 2015 and max value 2023
    Any other fields you would like to include in car model
    __str__ method to print a car make object
    '''
    # Many-to-One relationship
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'coupe'),
        ('HATCHBACK', 'Hatchback'),
        ('MUSCLE', 'Muscle'),
        ('JEEP', 'Jeep'),
        # Add more choices as required
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2024,
        validators=[
            MaxValueValidator(2024),
            MinValueValidator(2015)
        ])
    # Other fields as needed
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.name  # Return the name as the string representation
