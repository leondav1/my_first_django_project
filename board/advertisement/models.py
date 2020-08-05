from django.db import models


# Create your models here.
class Advertisement(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=1500, db_index=True)
    description = models.TextField(verbose_name='Описание', default='')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    price = models.FloatField(verbose_name='Цена', default=0)
    views_count = models.IntegerField(verbose_name='Количество просмотров', default=0)
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, on_delete=models.CASCADE, related_name='adv_status')
    type = models.ForeignKey('AdvertisementType', default=None, null=True, on_delete=models.CASCADE, related_name='adv_type')

    def __str__(self):
        return self.title


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AdvertisementType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
