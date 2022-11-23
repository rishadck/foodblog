

# Createmoduls
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
 
class catg(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
     
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

      


    def get_url(self): 
        return reverse('prod_cat',args=[self.slug])
 

    def __str__(self):
        return '{}'.format(self.name)

class product(models.Model):
    
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    img=models.ImageField(upload_to='sss')
   
    price=models.IntegerField()
    avilable=models.BooleanField()
    stock=models.IntegerField()
    disc=models.TextField()
    catagory=models.ForeignKey(catg,on_delete=models.CASCADE)
    
    def get_url(self):
        return reverse('details',args=[self.catagory.slug,self.slug]) 

    def __str__(self) -> str:
        return '{}'.format(self.name) 
