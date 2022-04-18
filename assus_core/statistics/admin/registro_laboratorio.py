# -*- coding: utf-8 -*-

from django.contrib import admin

from assus_core.statistics.models import RegistroLaboratorioORM


@admin.register(RegistroLaboratorioORM)
class RegistroLaboratorioAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'paciente',
        'se_tomo_muestra',
        'razon_rechazo',
        'tipo_muestra',
        'fecha_toma_muestra',
        'fecha_envio_muestra',
        'resultado',
    )
    raw_id_fields = ('paciente', )
    search_fields = (
        'paciente__nombres',
        'paciente__ap_paterno',
    )
    list_filter = (
        'resultado',
    )
