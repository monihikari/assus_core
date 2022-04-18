# -*- coding: utf-8 -*-

from django.contrib import admin

from assus_core.statistics.models import AntecedenteORM


@admin.register(AntecedenteORM)
class AntecedenteAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'paciente',
        'tipo_ocupacion',
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
