# Generated by Django 2.0.4 on 2018-06-08 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180608_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='short_description',
            field=models.CharField(default='Please enter a short description', max_length=200, unique=True),
            preserve_default=False,
        ),
    ]