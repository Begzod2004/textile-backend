# Generated by Django 4.2.2 on 2023-06-24 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_application_email_application_image_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='image_1',
        ),
        migrations.RemoveField(
            model_name='application',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='application',
            name='image_3',
        ),
        migrations.RemoveField(
            model_name='application',
            name='image_4',
        ),
        migrations.RemoveField(
            model_name='application',
            name='image_5',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_5',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]