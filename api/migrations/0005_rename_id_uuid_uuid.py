# Generated by Django 4.0.1 on 2022-01-16 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_uuid_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uuid',
            old_name='id',
            new_name='uuid',
        ),
    ]
