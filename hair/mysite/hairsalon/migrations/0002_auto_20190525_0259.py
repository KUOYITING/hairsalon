# Generated by Django 2.0 on 2019-05-24 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hairsalon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designer',
            name='dayoff',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='designer',
            name='workinghour',
            field=models.CharField(max_length=20),
        ),
    ]
