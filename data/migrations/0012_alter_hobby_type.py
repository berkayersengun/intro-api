# Generated by Django 4.1.5 on 2023-01-22 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_alter_food_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobby',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data.hobbytype'),
        ),
    ]
