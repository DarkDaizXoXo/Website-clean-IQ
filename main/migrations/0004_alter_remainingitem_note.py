# Generated by Django 5.0.2 on 2024-02-28 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remainingitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remainingitem',
            name='note',
            field=models.CharField(max_length=100),
        ),
    ]
