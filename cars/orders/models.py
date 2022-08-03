from ctypes import sizeof
from django.db import models
# * [get_user_model] helps us to get our user model even without calling our user model.
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Order(models.Model):
    
    BRANDS = (
        ('TOYOTA', 'toyota'),
        ('CHEVROLET', 'chevrolet'),
        ('HONDA', 'honda'),
        ('FORD', 'ford'),
        ('FIAT', 'fiat'),
        ('JEEP', 'jeep'),
        ('VOLKSWAGEN', 'volkswagen'),
        ('VOLVO', 'volvo'),
        ('AUDI', 'audi'),
        ('LAND_ROVER', 'landrover'),
        ('LEXUS', 'lexus'),
        ('PORSHE', 'porshe'),
        ('BUGATTI', 'bugatti'),
    )
    
    ORDER_STATUS = (
        'PENDING', 'pending',
        'IN_TRANSIT', 'intransit',
        'DELIVERED', 'delivered',
    )
    
    customer           = models.ForeignKey(User, on_delete=models.CASCADE)
    size               = models.CharField(max_length = 20, choices=SIZES)
    # cars_description = 