from rest_framework import serializers
from website.models import Customers, Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__' #['id', 'name', 'description', 'price', 'stock']
        read_only_fields = ['id', 'name']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'address', 'city', 'country', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
