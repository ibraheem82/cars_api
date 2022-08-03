
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
        ('PORSCHE', 'porsche'),
        ('BUGATTI', 'bugatti'),
        ('NISSAN', 'nissan'),
        ('JAGUAR', 'jaguar'),
        ('BENTLEY', 'bentley'),
        ('ROLLS_ROYCE', 'rollsroyce'),
        
        
    )
    
    ORDER_STATUS = (
        ('PENDING', 'pending'),
        ('IN_TRANSIT', 'intransit'),
        ('DELIVERED', 'delivered'),
    )
    
    customer           = models.ForeignKey(User, on_delete=models.CASCADE)
    brand              = models.CharField(max_length = 20, choices=BRANDS, default=BRANDS[0][0])
    order_status       = models.CharField(max_length=20, choices=ORDER_STATUS, default=ORDER_STATUS[0][0])
    quantity           = models.IntegerField()
    cars_description   = models.TextField(null=True, blank=True)
    cars_images        = models.ImageField()
    created_at         = models.DateTimeField(auto_now_add=True)
    updated_at         = models.DateTimeField(auto_now = True)




    def __str__(self):
        return f"<Order {self.brand} by {self.customer.id}"