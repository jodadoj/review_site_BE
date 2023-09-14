from django.contrib.auth.models import User, Group
from rest_framework import serializers
from reviews.models import Business, Category, Review

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
             model = Group
             fields = ['url', 'name']
             
class BusinessSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
             model = Business
             fields = '__all__'
             
class CategorySerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
             model = Category
             fields = '__all__'
             
class ReviewSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
             model = Review
             fields = '__all__'