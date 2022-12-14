# Generated by Django 4.0.3 on 2022-09-18 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mebel', '0016_barnie_stulya_cresla_crovati_divani_stoli_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='postimage',
            name='barnie_stulya',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mebel.barnie_stulya'),
        ),
        migrations.AddField(
            model_name='postimage',
            name='cresla',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mebel.cresla'),
        ),
        migrations.AddField(
            model_name='postimage',
            name='divani',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mebel.divani'),
        ),
        migrations.AddField(
            model_name='postimage',
            name='krovati',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mebel.crovati'),
        ),
        migrations.AddField(
            model_name='postimage',
            name='stoli',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mebel.stoli'),
        ),
        migrations.AddField(
            model_name='postimage',
            name='stulia',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mebel.stulia'),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='images',
            field=models.FileField(upload_to='mebel/images/'),
        ),
    ]
