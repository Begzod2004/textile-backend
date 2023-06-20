from rest_framework import generics
from .models import Category, Product, Statistics, Application
from .serializers import CategorySerializer, ProductSerializer, StatisticsSerializer, ApplicationSerializer

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
