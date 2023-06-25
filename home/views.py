from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Product, Statistics, Application, AboutUs
from .serializers import CategorySerializer, ProductSerializer, StatisticsSerializer, ApplicationSerializer, \
    AboutUsSerializer


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class StatisticsListCreateView(generics.ListCreateAPIView):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer


class ApplicationListView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class AboutUsListView(generics.ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class AboutUsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
