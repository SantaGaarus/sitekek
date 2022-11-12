# Generated by Django 4.0.3 on 2022-09-18 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mebel', '0015_stulia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barnie_stulya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название ')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('image', models.ImageField(upload_to='mebel/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Cresla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название ')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('image', models.ImageField(upload_to='mebel/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Crovati',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название ')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('image', models.ImageField(upload_to='mebel/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Divani',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название ')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('image', models.ImageField(upload_to='mebel/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Stoli',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название ')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('image', models.ImageField(upload_to='mebel/images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='mebel',
            name='type_mebel',
        ),
        migrations.RemoveField(
            model_name='stulia',
            name='type_mebel',
        ),
        migrations.AlterField(
            model_name='mebel',
            name='title',
            field=models.CharField(max_length=150, verbose_name='название '),
        ),
        migrations.AlterField(
            model_name='stulia',
            name='title',
            field=models.CharField(max_length=150, verbose_name='название '),
        ),
    ]