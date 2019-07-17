from django.db import models
from django.db.models import Q
import random, os
from django.db.models.signals import pre_save
from django.urls import reverse

from .utils import unique_slug_generator

# Create your models here.

def get_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def image_path(instance, filename):
    new_filename = random.randint(0, 123421452)
    name, ext = get_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'products/{new_filename}{final_filename}'


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def search(self, query):
        lookups = (Q(title__icontains=query)
                   | Q(description__icontains=query)
                   | Q(price__icontains=query)
                   | Q(tag__title__icontains=query)
                   )
        return self.filter(lookups).distinct()

class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):
        return self.get_queryset().filter(featured=True)

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)

class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    image = models.ImageField(upload_to=image_path, null=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ProductManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug':self.slug})


def product_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save, sender=Product)
