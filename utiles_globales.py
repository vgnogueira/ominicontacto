# -*- coding: utf-8 -*-
# Copyright (C) 2018 Freetech Solutions

# This file is part of OMniLeads

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/.
#

from __future__ import unicode_literals

from django.db import connection
from django.forms import ValidationError
from django.utils.translation import ugettext as _

from ominicontacto_app.errors import OmlArchivoImportacionInvalidoError
from ominicontacto_app.models import CalificacionCliente


def validar_extension_archivo_audio(valor):
    if valor is not None and not valor.name.endswith('.wav'):
        raise ValidationError(_('Archivos permitidos: .wav'), code='invalid')


def obtener_cantidad_no_calificados(total_llamadas_qs, fecha_desde, fecha_hasta, campana):
    total_llamadas_campanas = total_llamadas_qs.count()
    total_calificados = CalificacionCliente.history.filter(
        fecha__range=(fecha_desde, fecha_hasta),
        opcion_calificacion__campana=campana, history_change_reason='calificacion').count()
    total_atendidas_sin_calificacion = total_llamadas_campanas - total_calificados
    if total_atendidas_sin_calificacion < 0:
        # significa que el agente calificó llamadas que no conectaron con el usuario
        total_atendidas_sin_calificacion = 0
    return total_atendidas_sin_calificacion


def validar_estructura_csv(data_csv_memory, err_message, logger):
    """Analiza si un archivo con extensión .csv tiene una estructura válida"""
    try:
        # chequea que el csv tenga un formato estándar de black list, así podemos descartar
        # archivos csv corruptos
        all([row[0] < row[1] for row in data_csv_memory])
    except Exception as e:
        logger.warn("Error: {0}".format(e.message))
        raise(OmlArchivoImportacionInvalidoError(err_message))


def obtener_sip_agentes_sesiones_activas_kamailio():
    cursor = connection.cursor()
    sql = "select username from location"
    cursor.execute(sql)
    values = cursor.fetchall()
    result = [int(value[0]) for value in values]
    return result
