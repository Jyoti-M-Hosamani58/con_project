# Generated by Django 5.0.6 on 2024-07-09 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consignment_app', '0004_alter_addconsignment_desc_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='addconsignment',
            name='Consignment_id',
            field=models.IntegerField(max_length=50, null=True),
        ),
    ]
