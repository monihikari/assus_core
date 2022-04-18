# -*- coding: utf-8 -*-

from django.contrib import admin

from assus_core.statistics.models import EstablecimientoORM


@admin.register(EstablecimientoORM)
class EstablecimientoAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'nombre',
        'cod_establecimiento',
        'red_salud',
    )
    raw_id_fields = ('direccion', )
    search_fields = (
        'nombre',
        'cod_establecimiento',
    )
    list_filter = (
        'creacion',
    )
