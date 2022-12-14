# Generated by Django 4.0.3 on 2022-09-20 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mebel', '0028_stulia_derevosn_stulia_ecokoja_stulia_obivpecg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barnie_stulya',
            name='deep_stul',
            field=models.CharField(max_length=150, verbose_name='Глубина общая'),
        ),
        migrations.AlterField(
            model_name='barnie_stulya',
            name='depp_sid',
            field=models.CharField(max_length=150, verbose_name='Глубина сиденья'),
        ),
        migrations.AlterField(
            model_name='barnie_stulya',
            name='height_obj',
            field=models.CharField(max_length=150, verbose_name='Высота общая'),
        ),
        migrations.AlterField(
            model_name='barnie_stulya',
            name='height_stul',
            field=models.CharField(max_length=150, verbose_name='Высота сиденья'),
        ),
        migrations.AlterField(
            model_name='barnie_stulya',
            name='width_stul',
            field=models.CharField(max_length=150, verbose_name='Ширина сиденья'),
        ),
        migrations.AlterField(
            model_name='cresla',
            name='deep',
            field=models.CharField(max_length=150, verbose_name='Глубина'),
        ),
        migrations.AlterField(
            model_name='cresla',
            name='height_obj',
            field=models.CharField(max_length=150, verbose_name='Высота общая'),
        ),
        migrations.AlterField(
            model_name='cresla',
            name='height_ott',
            field=models.CharField(max_length=150, verbose_name='Высота оттоманки'),
        ),
        migrations.AlterField(
            model_name='cresla',
            name='height_sid',
            field=models.CharField(max_length=150, verbose_name='Высота сиденья'),
        ),
        migrations.AlterField(
            model_name='cresla',
            name='ott_dlin',
            field=models.CharField(max_length=150, verbose_name='Длина'),
        ),
        migrations.AlterField(
            model_name='cresla',
            name='ott_width',
            field=models.CharField(max_length=150, verbose_name='Ширина'),
        ),
        migrations.AlterField(
            model_name='cresla',
            name='width',
            field=models.CharField(max_length=150, verbose_name='Ширина'),
        ),
        migrations.AlterField(
            model_name='crovati',
            name='dlina_width',
            field=models.CharField(max_length=150, verbose_name='Длина общая:'),
        ),
        migrations.AlterField(
            model_name='crovati',
            name='height_izg',
            field=models.CharField(max_length=150, verbose_name='Высота изголовь'),
        ),
        migrations.AlterField(
            model_name='crovati',
            name='height_izn',
            field=models.CharField(max_length=150, verbose_name='Высота изножья'),
        ),
        migrations.AlterField(
            model_name='crovati',
            name='width',
            field=models.CharField(max_length=150, verbose_name='Ширина'),
        ),
        migrations.AlterField(
            model_name='divani',
            name='deep',
            field=models.CharField(max_length=150, verbose_name='Глубина'),
        ),
        migrations.AlterField(
            model_name='divani',
            name='deepSidBezPod',
            field=models.CharField(max_length=150, verbose_name='Глубина сиденья без подушек'),
        ),
        migrations.AlterField(
            model_name='divani',
            name='height',
            field=models.CharField(max_length=150, verbose_name='Высота'),
        ),
        migrations.AlterField(
            model_name='divani',
            name='heightPod',
            field=models.CharField(max_length=150, verbose_name='Высота подлокотника'),
        ),
        migrations.AlterField(
            model_name='divani',
            name='heightSid',
            field=models.CharField(max_length=150, verbose_name='Высота сиденья'),
        ),
        migrations.AlterField(
            model_name='divani',
            name='width',
            field=models.CharField(max_length=150, verbose_name='Ширина'),
        ),
    ]
