# Generated by Django 3.1.7 on 2021-03-16 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicWorks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iswc', models.CharField(max_length=50, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('contributors', models.CharField(max_length=300)),
            ],
        ),
    ]
