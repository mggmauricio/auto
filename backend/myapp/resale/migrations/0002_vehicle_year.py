# Generated by Django 3.2.9 on 2021-11-24 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resale', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='year',
            field=models.IntegerField(default=2021),
        ),
    ]