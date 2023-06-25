from django.urls import path
from .views import  StatisticsListCreateView, \
    ApplicationListView, ApplicationDetailView, ProductListView, ProductDetailView, AboutUsListView, \
    AboutUsDetailView, CategoryListView, CategoryDetailView
from .CastomSort import CustomAPISorter

api_sorter = CustomAPISorter()

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-list-create'),
    path('statistics/', StatisticsListCreateView.as_view(), name='statistics-list-create'),
    path('applications/', ApplicationListView.as_view(), name='application-list'),
    path('applications/<int:pk>/', ApplicationDetailView.as_view(), name='application-detail'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('about-us/', AboutUsListView.as_view(), name='about-us-list'),
    path('about-us/<int:pk>/', AboutUsDetailView.as_view(), name='about-us-detail'),
]

urlpatterns = api_sorter.sort_apis(urlpatterns)


