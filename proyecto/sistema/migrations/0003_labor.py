# Generated by Django 4.2.6 on 2023-11-12 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0002_ambiente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Labor',
            fields=[
                ('id_labor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_labor', models.CharField(max_length=100)),
                ('tipo_labor', models.CharField(max_length=30)),
            ],
        ),
    ]
