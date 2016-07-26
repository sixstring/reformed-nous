# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 17:06
from __future__ import unicode_literals

import datetime
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [('nous', '0003_auto_20160725_0941'), ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(
                    2016, 7, 26, 17, 6, 35, 274196, tzinfo=utc
                )
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='modified_at',
            field=models.DateTimeField(
                auto_now=True,
                default=datetime.datetime(
                    2016, 7, 26, 17, 6, 37, 45736, tzinfo=utc
                )
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resource',
            name='created_at',
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(
                    2016, 7, 26, 17, 6, 39, 240182, tzinfo=utc
                )
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resource',
            name='modified_at',
            field=models.DateTimeField(
                auto_now=True,
                default=datetime.datetime(
                    2016, 7, 26, 17, 6, 41, 817517, tzinfo=utc
                )
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='created_at',
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(
                    2016, 7, 26, 17, 6, 44, 863622, tzinfo=utc
                )
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='modified_at',
            field=models.DateTimeField(
                auto_now=True,
                default=datetime.datetime(
                    2016, 7, 26, 17, 6, 47, 40234, tzinfo=utc
                )
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resource',
            name='details',
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True, default='{}'
            ),
            preserve_default=False,
        ),
    ]
