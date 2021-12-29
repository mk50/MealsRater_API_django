from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from . import views
router=routers.DefaultRouter()
router.register('meal',views.MealViewSet)
router.register('rating',views.RatingViewSet)
router.register('users',views.UsrViewSet)

urlpatterns = [
    path('',include(router.urls)),
  
    
]
