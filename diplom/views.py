from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import action

from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response


class OrderListInfoView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=True)
    def personal_orders(self, request, pk=None):
        queryset = Order.objects.filter(IDCourier=pk)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CourierInfoView(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer


class VendorInfoView(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class CustomUserInfoView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


## перенести на курьера, сделать локальное хранилище, сделать время,