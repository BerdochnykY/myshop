from django.db import models


class ProductCategory(models.Model):
    category = models.CharField('Категория', max_length=64, null=True, blank=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.category

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'

class Product(models.Model):
    name = models.CharField('Имя товара', max_length = 200, null=True, blank=True, default=None)
    price = models.DecimalField('Цена', max_digits=8, decimal_places=2, default=0)
    discount = models.IntegerField('Скидка', default=0)
    type = models.ForeignKey(ProductCategory, null=True, blank=True, default=None, on_delete = models.CASCADE)
    short_description = models.TextField('Короткое описание', null=True, blank=True, default=None)
    description = models.TextField('Полное описание', null=True, blank=True, default=None)
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
    image = models.ImageField(upload_to='products_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фоторграфии'
