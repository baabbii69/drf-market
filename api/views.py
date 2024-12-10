from .models import *
from api.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import  ModelViewSet
from rest_framework.generics import ListCreateAPIView


class ProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    # def put(self, request, *args, **kwargs):
    #     serializer = ProductSerializer(request.data)
    #     if serializer.is_valid():
    #         try:
    #             product = Product.objects.get(pk=kwargs['pk'])
    #         except:
    #             return Response({"error": "Product doesn't exist"})
    #
    #


class OrderList(APIView):
    def get(self, request, *args, **kwargs):
        products = Order.objects.all()
        serializer = OrderSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request,*args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderListAPIView(ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)