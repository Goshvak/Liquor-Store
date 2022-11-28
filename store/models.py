from django.db import models
from django.core.validators import MaxValueValidator 

class Review(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    review = models.CharField(max_length=500)
    
    def __str__(self):
        return f'Review from {self.email}'
    
class ItemsModel(models.Model):
    item_name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    year = models.IntegerField(validators=[MaxValueValidator(9999)])
    price = models.IntegerField(validators=[MaxValueValidator(9999)])
    image = models.ImageField(upload_to='media/image')
    
    def __str__(self):
        return self.item_name
    