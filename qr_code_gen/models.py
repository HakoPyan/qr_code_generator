from django.db import models

# Create your models here.
class QR_Data(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone_number = models.PositiveIntegerField()
    email = models.EmailField(max_length=254)
    qr = models.ImageField(upload_to="media/")

    def __str__(self):
        return f"{self.name} {self.surname}, phone: {self.phone_number}, email: {self.email}"