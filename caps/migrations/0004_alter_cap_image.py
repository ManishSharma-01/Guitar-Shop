# Generated by Django 4.0.5 on 2022-07-21 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caps', '0003_cap_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cap',
            name='image',
            field=models.ImageField(upload_to='savedImages'),
        ),
    ]
