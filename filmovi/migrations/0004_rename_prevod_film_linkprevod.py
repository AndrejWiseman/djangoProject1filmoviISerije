# Generated by Django 4.2.7 on 2023-11-28 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmovi', '0003_film_prevod'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='prevod',
            new_name='linkPrevod',
        ),
    ]
