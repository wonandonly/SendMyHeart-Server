# Generated by Django 4.2.7 on 2023-11-17 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0003_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='/default.jpg', upload_to='', verbose_name='이미지'),
        ),
    ]
