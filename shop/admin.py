from django.contrib import admin
from .models import *

# Register your models here.
class productadmin(admin.ModelAdmin):
    list_display=['name','slug','price','img','stock','avilable']
    list_editable=['price','stock','img','avilable']
    prepopulated_fields={'slug':('name',)}
admin.site.register(product,productadmin)
class catgadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
admin.site.register(catg,catgadmin )