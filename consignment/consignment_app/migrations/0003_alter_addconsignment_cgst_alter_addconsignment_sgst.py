# Generated by Django 5.0.6 on 2024-07-09 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consignment_app', '0002_alter_addconsignment_cgst_alter_addconsignment_gst_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addconsignment',
            name='cgst',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='addconsignment',
            name='sgst',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
