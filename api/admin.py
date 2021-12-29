from django.contrib import admin
from .models import *

class Ratingadmin(admin.ModelAdmin):
    list_display=['id','meal','user','stars']
    list_filter=['meal','user']

class Mealadmin(admin.ModelAdmin):
    list_display=['id','title','description']
    list_filter=['title','description']
    search_fields=['title','description']
 
admin.site.register(Rating,Ratingadmin)
admin.site.register(Meal,Mealadmin)