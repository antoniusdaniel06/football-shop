from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
    ('jersey', 'Jersey'),
    ('sepatu', 'Sepatu'),
    ('peralatan', 'Peralatan Olahraga'),
    ('aksesoris', 'Aksesoris'),
    ('bola', 'Bola'),
    ('lainnya', 'Lainnya'),
]

    name = models.CharField(max_length=50)  
    price = models.IntegerField() 
    description = models.TextField()  
    thumbnail = models.URLField()  
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES,default='update')  
    is_featured = models.BooleanField(default=False)  

    def __str__(self):
        return self.name
    