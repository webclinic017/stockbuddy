# Generated by Django 3.0.5 on 2020-06-12 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockbuddy', '0004_auto_20200612_1330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockdata',
            old_name='prediction3',
            new_name='mlprediction',
        ),
    ]