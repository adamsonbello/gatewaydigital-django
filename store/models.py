from django.urls import reverse
from django.db import models
from category.models import Category
from ckeditor.fields import RichTextField


class Product(models.Model):
    product_name = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, unique=False, blank=True)
    subtitle1 = models.CharField(max_length=255, unique=False, blank=True)
    subtitle2 = models.CharField(max_length=255, unique=False, blank=True)
    slug = models.SlugField(unique=True)
    intro_description = RichTextField(blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    description_2 = RichTextField(blank=True, null=True)
    description_3 = RichTextField(blank=True, null=True)
    product_img = models.ImageField(upload_to='photos/products')
    product_img_2 = models.ImageField(upload_to='photos/products', blank=True)
    product_img_3 = models.ImageField(upload_to='photos/products', blank=True)
    product_img_4 = models.ImageField(upload_to='photos/products', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return  '%s %s %s %s' % (self.product_name, self.category, self.date_created, self.date_modified)
    
    
   