# Generated by Django 2.1.3 on 2018-11-17 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_article_head_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='head_img',
            field=models.ImageField(upload_to='uploads', verbose_name='文章标题图片'),
        ),
    ]
