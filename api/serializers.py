from rest_framework import fields, serializers
from .models import *
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password']
        extra_kwargs={'password':{'write_only':True,'required':True}}

class MealSerializers(serializers.ModelSerializer):
    class Meta:
        model=Meal
        fields=['id','title','description','num_rating','avg_rating']

class RateSerializers(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields=['id','stars','user','meal']