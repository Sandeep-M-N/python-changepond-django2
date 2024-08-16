from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify

# Create your models here.
class Author(models.Model):
    First_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100,null=True)
    age = models.IntegerField(validators=[MaxValueValidator(60), MinValueValidator(18)], null=True)
    rating = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(2)], null=True)
    full_name=models.CharField(max_length=60,null=True,editable=False)
    #jk rowling ===> jk-rowling
    slug=models.SlugField(default='',db_index=True,editable=False)
    # sugify used to take all letters into small letters and spaces to '-'
    def save(self, *args, **kwargs):
        self.full_name= f'{self.First_name} {self.last_name}'
        self.slug=slugify(self.full_name)
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.First_name}  {self.last_name}"

    