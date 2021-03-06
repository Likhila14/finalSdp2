# Generated by Django 3.1.4 on 2021-05-18 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_auto_20210518_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='cam',
        ),
        migrations.RemoveField(
            model_name='review',
            name='ent',
        ),
        migrations.RemoveField(
            model_name='review',
            name='loc',
        ),
        migrations.RemoveField(
            model_name='review',
            name='nop',
        ),
        migrations.RemoveField(
            model_name='review',
            name='noti',
        ),
        migrations.AddField(
            model_name='book',
            name='cam',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='ent',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='loc',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='nop',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='noti',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
