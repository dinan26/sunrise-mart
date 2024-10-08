from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["nama", "deskripsi", "stock", "harga" ]

    def clean_nama(self):
        nama = self.cleaned_data["nama"]
        return strip_tags(nama)

    def clean_deskripsi(self):
        deskripsi = self.cleaned_data["deskripsi"]
        return strip_tags(deskripsi)
    
    def clean_stock(self):
        stock = self.cleaned_data["stock"]
        return strip_tags(stock)
    
    def clean_harga(self):
        harga = self.cleaned_data["harga"]
        return strip_tags(harga)
    
   
    
