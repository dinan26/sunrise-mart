import uuid
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama = models.CharField(max_length = 255)
    deskripsi = models.TextField()
    stock =  models.IntegerField()
    harga = models.IntegerField()
   