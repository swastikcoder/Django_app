# Generated by Django 5.1.3 on 2024-11-20 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='banner',
            field=models.ImageField(default='fallback.png', upload_to=''),
        ),
    ]
