# Generated by Django 4.1.2 on 2022-11-12 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mebel', '0039_alter_crovati_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='divani',
            name='description',
            field=models.TextField(max_length=2000, verbose_name='Описание'),
        ),
    ]
