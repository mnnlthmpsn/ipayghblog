# Generated by Django 3.0.5 on 2020-04-29 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.CharField(default='localhost:8000', max_length=1000),
        ),
    ]