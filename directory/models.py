from django.db import models
from django.urls import reverse

class AddressBook(models.Model):
    first_name = models.CharField(max_length=128)
    second_name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128, blank=True)
    phone_number = models.CharField(max_length=28)
    email = models.EmailField(max_length=254)
    photo = models.ImageField(upload_to='uploads/', blank=True)
    birth_date = models.DateField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.second_name}'
    
    def get_absolute_url(self):
        return reverse('address-detail', args=[str(self.id)])