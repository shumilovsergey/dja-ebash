# Generated by Django 5.0.1 on 2024-01-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=20)),
                ('author_id', models.IntegerField(default=0)),
                ('body', models.TextField(default=None)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('color', models.CharField(default='0', max_length=20)),
                ('url', models.CharField(default=None, max_length=256)),
            ],
            options={
                'ordering': ['-updated'],
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=20)),
                ('author_id', models.IntegerField(default=0)),
                ('body', models.JSONField(default=None)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('url', models.CharField(default=None, max_length=256)),
            ],
            options={
                'ordering': ['-updated'],
            },
        ),
    ]
