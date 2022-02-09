# Generated by Django 3.2.9 on 2021-11-24 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resale', '0002_vehicle_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryCosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='vehicle',
            name='costs',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='manufacter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='resale.manufacter'),
        ),
        migrations.CreateModel(
            name='Costs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='resale.categorycosts')),
            ],
        ),
    ]
