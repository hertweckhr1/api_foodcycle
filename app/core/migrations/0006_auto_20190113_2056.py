# Generated by Django 2.1.5 on 2019-01-13 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190109_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='status',
            field=models.CharField(default='posted', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='company_logo_image',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
