# Generated by Django 3.2.2 on 2021-05-31 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0007_auto_20210523_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='boost',
            name='boost_type',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='maincycle',
            name='autoClickPower',
            field=models.IntegerField(default=0),
        ),
    ]