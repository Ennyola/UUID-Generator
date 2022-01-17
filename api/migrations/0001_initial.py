# Generated by Django 4.0.1 on 2022-01-15 16:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UUID',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('time_stamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
