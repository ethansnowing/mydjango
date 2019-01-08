# Generated by Django 2.1.3 on 2018-12-19 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_auto_20181219_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='avg_frame_rate',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, verbose_name='平均帧率'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='bit_rate',
            field=models.IntegerField(blank=True, default=0, verbose_name='码率'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='duration',
            field=models.IntegerField(blank=True, default=-1, verbose_name='时长'),
            preserve_default=False,
        ),
    ]