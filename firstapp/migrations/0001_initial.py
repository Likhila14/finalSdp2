# Generated by Django 3.1.4 on 2021-05-17 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anniversary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('img', models.ImageField(upload_to='pics')),
                ('price', models.IntegerField()),
                ('rate', models.IntegerField()),
            ],
            options={
                'db_table': 'anniversary',
            },
        ),
        migrations.CreateModel(
            name='Birthday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('img', models.ImageField(upload_to='pics')),
                ('price', models.IntegerField()),
                ('rate', models.IntegerField()),
            ],
            options={
                'db_table': 'birthday',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=80)),
                ('ename', models.CharField(max_length=80)),
                ('price', models.IntegerField()),
                ('phnno', models.IntegerField()),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'bookingdetails',
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'registers',
            },
        ),
    ]
