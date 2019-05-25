# Generated by Django 2.0 on 2019-05-25 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hairsalon', '0002_auto_20190525_0259'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookingItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemID', models.DecimalField(decimal_places=0, max_digits=20, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('phone', models.DecimalField(decimal_places=0, max_digits=15)),
                ('itemName', models.CharField(max_length=20)),
                ('orderQuantity', models.DecimalField(decimal_places=0, max_digits=2)),
                ('orderPrice', models.DecimalField(decimal_places=1, max_digits=5)),
            ],
        ),
        migrations.RenameField(
            model_name='designer',
            old_name='name',
            new_name='designerName',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='cost',
            new_name='itemCost',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='itemName',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='price',
            new_name='itemPrice',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='quantity',
            new_name='itemQuantity',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='name',
            new_name='serviceName',
        ),
    ]
