from django.contrib.auth.models import User
from rest_framework import serializers
from myapp.models import Product


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['url', 'name', 'price', 'description', 'image', 'seller_name' ]
        
# class AddProductSerilizer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=True,max_length=100)
#     description = serializers.CharField(required=True,max_length=100)
#     price = serializers.IntegerField()
    
#     def create(self,validated_data):
        
        
#         return Product.objects.create(**validated_data)