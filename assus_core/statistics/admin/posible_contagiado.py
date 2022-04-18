# -*- coding: utf-8 -*-

from django.contrib import admin

from assus_core.statistics.models import PosibleContagiadoORM


@admin.register(PosibleContagiadoORM)
class PosibleContagiadoAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'nombres',
        'apellidos',
        'genero',
        'telefono',
    )
    raw_id_fields = ()
    search_fields = (
        'nombres',
        'apellidos',
        'telefono',
    )
    list_filter = (
        'genero',
    )
