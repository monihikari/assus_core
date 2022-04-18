# -*- coding: utf-8 -*-

from django.contrib import admin

from assus_core.statistics.models import FichaEpidemiologicaORM


@admin.register(FichaEpidemiologicaORM)
class FichaEpidemiologicaAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'establecimiento',
        'nombres_notificador',
        'apellidos_notificador',
        'telefonno_notificador',
        'fecha_notificacion',
        'semana_epidemiologica',
        'identificado_en_busqueda_activa',
    )
    raw_id_fields = (
        'establecimiento',
        'paciente',
        'antecedente',
        'registro_clinico',
        'hospitalizacion',
        'condicion_paciente',
        'registro_laboratorio',
    )
    search_fields = (
        'establecimiento__nombre',
        'establecimiento__cod_establecimiento',
        'nombres_notificador',
    )
    list_filter = (
        'creacion',
    )
