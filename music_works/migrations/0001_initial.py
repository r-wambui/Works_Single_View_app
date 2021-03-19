# Generated by Django 3.1.7 on 2021-03-18 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contributor', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MusicWorks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iswc', models.CharField(max_length=50, null=True, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('contributors', models.ManyToManyField(to='music_works.Contributor')),
            ],
        ),
    ]
