from django.contrib import admin
from .models import Category, Product, Statistics, Application, AboutUs


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']
    list_filter = ['category']
    search_fields = ['name']
    list_per_page = 20


class StatisticsAdmin(admin.ModelAdmin):
    list_display = ['count_looms', 'experience', 'bir_kunlik_chiqim']
    search_fields = ['count_looms']


# class ApplicationAdmin(admin.ModelAdmin):
#     list_display = ['name', 'phone_number', 'email', 'checked', 'date']
#     list_filter = ['checked']
#     search_fields = ['name', 'phone_number', 'email']
#     list_per_page = 50
#     readonly_fields = ['date']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Statistics, StatisticsAdmin)
# admin.site.register(Application, ApplicationAdmin)
from django.contrib import admin
from django.utils.html import format_html
from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email', 'display_checked', 'date']
    list_filter = ['checked']
    search_fields = ['name', 'phone_number', 'email']
    list_per_page = 50
    readonly_fields = ['date']

    def display_checked(self, obj):
        if obj.checked:
            return format_html('<span style="color: green;"><b>&#10004;</b></span>')  # Checked icon
        else:
            return format_html('<span style="color: red;"><b>&#10008;</b></span>')  # X icon

    display_checked.short_description = 'Checked'


admin.site.register(Application, ApplicationAdmin)


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('content',)
    fields = ('content',)
    readonly_fields = ('content',)

    def has_add_permission(self, request):
        # Disable the ability to add new AboutUs instances
        return False
