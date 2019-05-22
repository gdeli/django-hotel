from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Hotel(models.Model):

    Rating = (
        ('1', '1',),
        ('2', '2',),
        ('3', '3',),
        ('4', '4',),
        ('5', '5',),
    )

    nama = models.CharField(max_length=50)
    harga = models.IntegerField(default=0)
    provinsi = models.CharField(max_length=50)
    kota = models.CharField(max_length=50)
    kodepos = models.CharField(max_length=50)
    alamat = models.CharField(max_length=50)
    timestamp = models.DateTimeField(null=True)
    rating = models.CharField(max_length=9,choices=Rating,default=1)
    review = models.TextField()

    def __str__(self):
        return self.nama 

