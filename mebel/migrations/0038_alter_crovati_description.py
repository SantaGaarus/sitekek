# Generated by Django 4.1.2 on 2022-11-12 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mebel', '0037_delete_novinki_barnie_stulya_novinki_cresla_novinki_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crovati',
            name='description',
            field=models.CharField(max_length=20000, verbose_name='Описание'),
        ),
    ]
