# -*- coding: utf-8 -*-

from django.contrib import admin

from assus_core.statistics.models import CondicionPacienteORM


@admin.register(CondicionPacienteORM)
class CondicionPacienteAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'paciente',
        'tiene_hipertension',
        'tiene_obesisdad',
        'tiene_diabetes',
        'esta_embarazada',
    )
    raw_id_fields = ('paciente', )
    search_fields = (
        'paciente__doc_identidad',
        'paciente__nombres',
        'paciente__ap_paterno',
        'paciente__ap_materno',
    )
    list_filter = (
        'creacion',
    )
