# Generated by Django 5.1.6 on 2025-02-19 22:41

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_server', '0004_alter_manageaccount_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manageaccount',
            name='pass_key',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
