# Generated by Django 4.0 on 2022-10-10 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]