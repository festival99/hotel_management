from django.db import models

# Create your models here.
class Room(models.Model):
    Room_Categories=(
        ('YAC', 'AC'),
        ('NAC', 'NON-AC'),
        ('DEL', 'DELUXE'),
        ('KIN', 'KING'),
        ('QUE', 'QUEEN'),
    ) #left for database,Right to show
    
    number=models.IntegerField()
    category=models.CharField(max_length=3, choices=Room_Categories)
    beds=models.IntegerField()
    capacity=models.IntegerField()

    def __str__(self): #whenever you do something with your model it will show you this representation
        return f'{self.number}.{self.category} with {self.beds} beds for {self.capacity} people'