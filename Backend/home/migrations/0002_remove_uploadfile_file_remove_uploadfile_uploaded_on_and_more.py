# Generated by Django 5.0.2 on 2024-03-07 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfile',
            name='file',
        ),
        migrations.RemoveField(
            model_name='uploadfile',
            name='uploaded_on',
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
