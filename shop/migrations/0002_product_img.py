# Generated by Django 2.2 on 2022-11-12 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default='defualt.png', upload_to='sss'),
            preserve_default=False,
        ),
    ]