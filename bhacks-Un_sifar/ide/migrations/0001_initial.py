# Generated by Django 2.1.5 on 2019-03-09 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_id', models.CharField(max_length=255)),
                ('problem_content', models.TextField()),
                ('lang', models.CharField(max_length=255)),
                ('code_input', models.TextField()),
                ('compile_status', models.CharField(max_length=255)),
                ('run_status_status', models.CharField(max_length=255)),
            ],
        ),
    ]
