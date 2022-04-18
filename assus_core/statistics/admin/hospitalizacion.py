# -*- coding: utf-8 -*-

from django.contrib import admin

from assus_core.statistics.models import HospitalizacionORM


@admin.register(HospitalizacionORM)
class HospitalizacionAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'paciente',
        'estblecimiento',
        'es_ambulatorio',
        'es_internado',
    )
    raw_id_fields = (
        'paciente',
        'estblecimiento',
    )
    search_fields = (
        'municipio',
    )
    list_filter = (
        'creacion',
    )
