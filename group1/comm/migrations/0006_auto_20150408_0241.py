# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0005_auto_20150408_0108'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userroom',
            unique_together=set([('user', 'room')]),
        ),
    ]
