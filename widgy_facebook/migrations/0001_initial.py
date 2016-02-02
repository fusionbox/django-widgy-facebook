# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookPosts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('target', models.CharField(default=b'', help_text=b'Whose posts do you want to show?', max_length=255)),
                ('count', models.PositiveIntegerField(default=4, help_text=b'How many posts do you want to show?')),
                ('app_id', models.CharField(help_text=b'Found in the Facebook app dashboard.', max_length=255)),
                ('app_secret', models.CharField(help_text=b'Found in the same place as the app id.', max_length=255)),
            ],
        ),
    ]
