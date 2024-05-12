from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Nomi')
    slug = models.SlugField(verbose_name='Slug')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nomi')
    image = models.ImageField(upload_to='prducts/')
    description = models.TextField(verbose_name='Izoh')
    price = models.IntegerField(verbose_name='Narxi')
    discount = models.BooleanField(null=True)
    discount_procent = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategoriyasi')
    slug = models.SlugField(verbose_name='Slug')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'
