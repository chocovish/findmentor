# Generated by Django 2.1.6 on 2019-02-22 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20190222_2111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='bio',
            new_name='headline',
        ),
    ]
