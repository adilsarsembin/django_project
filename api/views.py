from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductsSerializer
from .models import Products


# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def products(request):
    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)

    elif request.method == 'POST':
        serializer = ProductsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

    return Response(serializer.data)


@api_view(['GET', 'POST', 'DELETE'])
def product(request, pk):
    product = Products.objects.get(id=pk)
    if request.method == 'GET':
        serializer = ProductsSerializer(product)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductsSerializer(instance=product, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    elif request.method == 'DELETE':
        product.delete()
        return Response('Item was successfully deleted')
