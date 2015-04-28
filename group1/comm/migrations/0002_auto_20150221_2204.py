# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='at_message',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='room',
            name='public',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='online',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
