# Generated by Django 4.2.5 on 2023-10-20 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=90)),
                ('phone', models.CharField(max_length=90)),
                ('message', models.CharField(max_length=2000)),
            ],
        ),
    ]
