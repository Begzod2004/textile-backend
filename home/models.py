from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=123, help_text="Назначение")
    image = models.ImageField(upload_to='media/')
    price = models.PositiveIntegerField()
    composition = models.CharField(max_length=123, help_text="Состав:")
    weight = models.CharField(max_length=123, help_text="Плотность")
    width = models.CharField(max_length=123, help_text="Ширина")
    length_per_kg = models.CharField(max_length=123, help_text="Длина на кг")
    minimum_order = models.CharField(max_length=123, help_text="Минимальный заказ")
    delivery_time = models.CharField(max_length=123, help_text="Срок поставки")

    def __str__(self):
        return self.name


class Statistics(models.Model):
    count_looms = models.CharField(max_length=123, help_text="считать ткацкие станки")
    experience = models.CharField(max_length=123, help_text="опыт")
    bir_kunlik_chiqim = models.CharField(max_length=200, help_text="тонн сырья в сутки")

    def __str__(self):
        return self.count_looms


class Application(models.Model):
    name = models.CharField(max_length=123, help_text="Nomi")
    phone_number = models.CharField(max_length=100, unique=True, help_text="Telefon raqami")
    email = models.EmailField(max_length=100, unique=True, help_text="Email")
    checked = models.BooleanField(default=False, help_text="Tekshirilganmi?")
    text = models.TextField(help_text="Matn")
    date = models.DateTimeField(auto_now_add=True, help_text="Sana")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class AboutUs(models.Model):
    content = models.TextField()

    def __str__(self):
        return "About Us"
