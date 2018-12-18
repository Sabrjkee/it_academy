from django.db import models


# Create your models here.
class MO (models.Model):
    name = models.CharField(
        max_length=255
    )
    phone_number = models.CharField(
        max_length=233
    )
    kod_mo = models.CharField(
        max_length=30
    )
    adress_mo = models.CharField(
        max_length=255
    )
    email_mo = models.EmailField(
        max_length=254
    )
    coordinates_google = models.TextField()


class PhotoMO (models.Model):
    mo = models.ForeignKey(
        MO,
        on_delete=models.CASCADE,
        #related_name="photomo",
    )
    photo = models.ImageField(
        upload_to='img/photo/%Y/%m/'
    )


