# Generated by Django 5.1.3 on 2024-11-20 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='banner',
            field=models.ImageField(default='fallback.jpg', upload_to=''),
        ),
    ]
