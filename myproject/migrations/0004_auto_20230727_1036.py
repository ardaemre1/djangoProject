# Generated by Django 3.2.20 on 2023-07-27 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0003_auto_20230726_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.CharField(default=1, max_length=200, verbose_name='Resim URL'),
            preserve_default=False,
        ),
    ]
