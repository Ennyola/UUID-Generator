# Generated by Django 4.0.1 on 2022-01-16 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_uuid_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uuid',
            options={'ordering': ['-time_stamp']},
        ),
    ]
