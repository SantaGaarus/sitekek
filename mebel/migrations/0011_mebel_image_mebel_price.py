# Generated by Django 4.0.3 on 2022-09-18 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mebel', '0010_alter_mebel_type_mebel'),
    ]

    operations = [
        migrations.AddField(
            model_name='mebel',
            name='image',
            field=models.ImageField(default=1, upload_to='mebel/images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mebel',
            name='price',
            field=models.IntegerField(default=1, verbose_name='цена'),
            preserve_default=False,
        ),
    ]
