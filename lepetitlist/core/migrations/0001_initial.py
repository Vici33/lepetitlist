# Generated by Django 4.2.4 on 2023-08-30 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(default='to do', max_length=255)),
                ('list_description', models.TextField(max_length=1000, null=True)),
                ('list_time', models.TimeField(null=True)),
            ],
        ),
    ]
