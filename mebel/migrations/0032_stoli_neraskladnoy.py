# Generated by Django 4.0.3 on 2022-09-21 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mebel', '0031_stoli_joutstoul'),
    ]

    operations = [
        migrations.AddField(
            model_name='stoli',
            name='neraskladnoy',
            field=models.BooleanField(default=1, verbose_name='НеРаскладной'),
            preserve_default=False,
        ),
    ]
