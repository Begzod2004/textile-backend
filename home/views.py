from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Product, Statistics, Application, AboutUs
from .serializers import CategorySerializer, ProductSerializer, StatisticsSerializer, ApplicationSerializer, \
    AboutUsSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class StatisticsListCreateView(generics.ListCreateAPIView):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer


class ApplicationListCreateView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


def post(request):
    serializer = AboutUsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


class AboutUsView(APIView):
    def get(self, request):
        about_us = AboutUs.objects.first()
        if about_us:
            serializer = AboutUsSerializer(about_us)
            return Response(serializer.data)
        else:
            return Response({'content': 'About Us content not found.'})

