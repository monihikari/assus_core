# -*- coding: utf-8 -*-

from django.contrib import admin

from assus_core.statistics.models import DireccionORM


@admin.register(DireccionORM)
class DireccionAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'pais',
        'departamento',
        'municipio',
        'ciudad',
    )
    raw_id_fields = ()
    search_fields = (
        'municipio',
    )
    list_filter = (
        'creacion',
    )
