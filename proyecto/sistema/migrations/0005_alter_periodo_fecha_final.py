# Generated by Django 4.2.6 on 2023-11-21 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0004_periodo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodo',
            name='fecha_final',
            field=models.DateField(blank=True, null=True),
        ),
    ]