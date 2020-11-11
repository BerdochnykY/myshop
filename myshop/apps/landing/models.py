from django.db import models

class Subscriber(models.Model):
    sub_name = models.CharField('Имя подписчика', max_length = 200)
    sub_email = models.EmailField('Почта')

    def __str__(self):
        return self.sub_name

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'
