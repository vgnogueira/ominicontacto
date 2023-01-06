# -*- coding: utf-8 -*-
# Copyright (C) 2018 Freetech Solutions

# This file is part of OMniLeads

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3, as published by
# the Free Software Foundation.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/.
#
# Generated by Django 1.9.7 on 2019-06-18 15:45

# El nombre de la migracion queda sin sentido ya que fue reemplazado su codigo
# por otro al simplificar la creacion de la tabla queue_log

from __future__ import unicode_literals

from django.db import migrations, connection


SQL_ALTER_DEFAULT = """
ALTER TABLE queue_log ALTER COLUMN time SET DEFAULT NULL;
ALTER TABLE queue_log ALTER COLUMN callid SET DEFAULT '';
ALTER TABLE queue_log ALTER COLUMN queuename SET DEFAULT '';
ALTER TABLE queue_log ALTER COLUMN agent SET DEFAULT '';
ALTER TABLE queue_log ALTER COLUMN event SET DEFAULT '';
ALTER TABLE queue_log ALTER COLUMN data1 SET DEFAULT '';
ALTER TABLE queue_log ALTER COLUMN data2 SET DEFAULT '';
ALTER TABLE queue_log ALTER COLUMN data3 SET DEFAULT '';
ALTER TABLE queue_log ALTER COLUMN data4 SET DEFAULT '';
ALTER TABLE queue_log ALTER COLUMN data5 SET DEFAULT '';
"""


def set_default_values_queue_log(apps, schema_editor):
    cursor = connection.cursor()
    cursor.execute(SQL_ALTER_DEFAULT)


class Migration(migrations.Migration):

    dependencies = [
        ('reportes_app', '0004_llamadalog_archivo_grabacion_length'),
    ]

    operations = [
        migrations.RunPython(
            set_default_values_queue_log, reverse_code=migrations.RunPython.noop)
    ]
