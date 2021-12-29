from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.serializers import Serializer
from .models import Rating,Meal
from .serializers import RateSerializers,MealSerializers, UserSerializers
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from rest_framework.authtoken.models import Token

class UsrViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializers
    authentication_classes=(TokenAuthentication,)
    permission_classes=(AllowAny,)

    # def create(self,validate_data):
    #     user=User.objects.create_user(**validated_data)
    #     token=Token.objects.create(user=user)
    #     return token


class MealViewSet(viewsets.ModelViewSet):
    queryset=Meal.objects.all()
    serializer_class=MealSerializers
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)

    @action(detail=True,methods=['POST'])
    def rate_meal(self,request,pk=None):
        if 'stars' in request.data:
            meal=Meal.objects.get(id=pk)
            user=request.user
            stars=request.data['stars']
            user=User.objects.get(username=user)
            try:
                rating=Rating.objects.get(user=user.id,meal=meal.id)
                rating.stars=stars
                rating.save()
                serializer=RateSerializers(rating,many=False)
                json={
                    'message':'rate update',
                    'result':serializer.data
                }

                return Response(json,status=status.HTTP_200_OK)
            except:
                rating=Rating.objects.create(
                    stars=stars,meal=meal,user=user

                )
                serializer=RateSerializers(rating,many=False)
                json={
                    'message':'rate created',
                    'result':serializer.data
                }
                return Response(json,status=status.HTTP_200_OK)


        else:
            json={
                'message':'rate not provider'
            }
            return Response(json,status=status.HTTP_400_BAD_REQUEST)

class RatingViewSet(viewsets.ModelViewSet):
    queryset=Rating.objects.all()
    serializer_class=RateSerializers
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        json={
            'mesaage':'this class dont allow update'
        }
        return Response(json,status=status.HTTP_400_BAD_REQUEST)
    def create(self, request, *args, **kwargs):
        json={
            'mesaage':'this class dont allow create'
        }
        return Response(json,status=status.HTTP_400_BAD_REQUEST)
