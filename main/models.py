import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama = models.CharField(max_length = 255)
    deskripsi = models.TextField()
    stock =  models.IntegerField()
    harga = models.IntegerField()
   