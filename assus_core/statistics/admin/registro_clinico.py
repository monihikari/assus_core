# -*- coding: utf-8 -*-

from django.contrib import admin

from assus_core.statistics.models import RegistroClinicoORM


@admin.register(RegistroClinicoORM)
class RegistroClinicoAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'paciente',
        'es_sintomatico',
        'fecha_inicio_intomas',
        'tiene_tos_seca',
        'tiene_fiebre',
    )
    raw_id_fields = ('paciente', )
    search_fields = (
        'paciente__nombres',
        'paciente__ap_paterno',
    )
    list_filter = (
        'es_sintomatico',
    )
