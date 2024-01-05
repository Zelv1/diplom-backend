from rest_framework import serializers
from .models import CustomUser, Courier, Order, Vendor


class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    courier = CourierSerializer(read_only=True)
    vendor = VendorSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'courier', 'vendor']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
