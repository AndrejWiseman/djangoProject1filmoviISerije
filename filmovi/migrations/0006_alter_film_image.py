# Generated by Django 4.2.7 on 2023-12-03 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmovi', '0005_alter_film_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]