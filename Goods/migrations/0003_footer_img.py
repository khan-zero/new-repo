# Generated by Django 3.2.12 on 2024-07-24 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0002_auto_20240724_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='img',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
