# -*- coding: utf-8 -*-

from django.contrib import admin

from assus_core.statistics.models import PacienteORM


@admin.register(PacienteORM)
class PacienteAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'doc_identidad',
        'tipo_doc_identidad',
        'fecha_nacimiento',
        'nombres',
        'ap_paterno',
        'ap_materno',
    )
    raw_id_fields = ('direccion', )
    search_fields = (
        'doc_identidad',
        'fecha_nacimiento',
        'nombres',
        'ap_paterno',
        'ap_materno',
    )
    list_filter = (
        'tipo_doc_identidad',
    )
