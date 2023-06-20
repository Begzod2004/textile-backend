from django.urls import path
from .views import CategoryListCreateView, ProductListCreateView, StatisticsListCreateView, ApplicationListCreateView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('statistics/', StatisticsListCreateView.as_view(), name='statistics-list-create'),
    path('applications/', ApplicationListCreateView.as_view(), name='application-list-create'),
]
