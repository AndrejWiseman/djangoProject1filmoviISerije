# Generated by Django 4.2.7 on 2023-11-28 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serija',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=250)),
                ('originalIme', models.CharField(blank=True, max_length=120, null=True)),
                ('zanr', models.CharField(max_length=200)),
                ('radnja', models.TextField(max_length=5000)),
                ('godina', models.CharField(max_length=10)),
                ('imdbOcena', models.CharField(max_length=100)),
                ('linkPreuzmi', models.CharField(max_length=1000)),
                ('linkGledaj', models.CharField(max_length=1000)),
                ('linkPrevod', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
    ]
