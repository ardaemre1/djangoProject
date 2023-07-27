from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Ürün Adı')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Fiyat')
    description = models.TextField(verbose_name='Açıklama')
    brand = models.CharField(max_length=50, verbose_name='Marka')
    stock_status = models.BooleanField(default=True, verbose_name='Stok Durumu')
    images = models.TextField(verbose_name='Resimler') 
    stock_quantity = models.PositiveIntegerField(default=0, verbose_name='Stok Miktarı')

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = 'Ürünler'
