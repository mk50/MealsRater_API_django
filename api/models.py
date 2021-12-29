from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

class Meal(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=250)

    def num_rating(self):
        rating=Rating.objects.filter(meal=self)
        return len(rating)
    def avg_rating(self):
        sum=0
        rating=Rating.objects.filter(meal=self)
        for x in rating:
            sum +=x.stars
        if len(rating)>0:
            return sum/len(rating)
        else:
            return 0

    def __str__(self):
        return self.title
    


class Rating(models.Model):
    meal=models.ForeignKey(Meal,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    stars=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return self.meal.title

    class Meta:
        unique_together=(('user','meal'),)
        index_together=(('user','meal'),)
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
