# Generated by Django 2.1.3 on 2018-12-19 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20181201_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='height',
            field=models.CharField(blank=True, max_length=16),
        ),
        migrations.AddField(
            model_name='video',
            name='width',
            field=models.CharField(blank=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='video',
            name='distinguishability',
            field=models.CharField(blank=True, max_length=16),
        ),
    ]