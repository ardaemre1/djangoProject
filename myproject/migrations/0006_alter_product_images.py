# Generated by Django 3.2.20 on 2023-07-27 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0005_auto_20230727_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.TextField(verbose_name='Resimler'),
        ),
    ]
