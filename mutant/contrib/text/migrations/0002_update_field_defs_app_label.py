# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import functools

from django.db import migrations


def _update_field_def_cts_app_label(from_app_label, to_app_label, apps, schema_editor):
    cts = apps.get_model('contenttypes', 'contenttype').objects
    model_names = [
        'charfielddefinition',
        'textfielddefinition',
    ]
    cts.filter(
        app_label=from_app_label, model__in=model_names
    ).update(app_label=to_app_label)


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            functools.partial(_update_field_def_cts_app_label, 'mutant', 'text'),
            functools.partial(_update_field_def_cts_app_label, 'text', 'mutant'),
        ),
        migrations.AlterModelTable(
            name='charfielddefinition',
            table=None,
        ),
    ]
