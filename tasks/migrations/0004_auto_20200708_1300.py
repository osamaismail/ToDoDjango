# Generated by Django 3.0.8 on 2020-07-08 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20200707_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
