# Generated by Django 2.0.7 on 2018-07-18 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180717_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bukutamu',
            name='gambar',
            field=models.ImageField(upload_to='gambar'),
        ),
    ]