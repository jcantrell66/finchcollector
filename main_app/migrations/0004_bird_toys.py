# Generated by Django 3.2.9 on 2022-01-26 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20220126_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='bird',
            name='toys',
            field=models.ManyToManyField(to='main_app.Toy'),
        ),
    ]