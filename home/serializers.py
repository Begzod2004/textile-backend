from rest_framework import serializers
from .models import Category, Product, Statistics, Application, AboutUs


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = '__all__'


# class ApplicationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Application
#         fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'
        # read_only_fields = ['content']
        # fields = '__all__'
        # exclude = ['content']
        # read_only_fields = ['content']


class ApplicationSerializer(serializers.ModelSerializer):
    checked_status = serializers.SerializerMethodField()

    class Meta:
        model = Application
        fields = ['id', 'name', 'phone_number', 'text', 'date',
                  'checked', 'checked_status']

    def get_checked_status(self, obj):
        if obj.checked:
            return "✅"
        else:
            return "❌"
