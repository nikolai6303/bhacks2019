# Generated by Django 2.1.5 on 2019-03-09 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_auto_20190309_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lectures',
            name='para',
        ),
        migrations.DeleteModel(
            name='para',
        ),
    ]
