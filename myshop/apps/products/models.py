from django.db import models

class Product(models.Model):
    name = models.CharField('Имя товара', max_length = 200, null=True, blank=True, default=None)
    price = models.DecimalField('Цена', max_digits=8, decimal_places=2, default=0)
    description = models.TextField('Описание', null=True, blank=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s, %s" % (self.price, self.name)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, default=None, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='myshop/static/media/products_images/')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фоторграфии'
