# -*- coding: utf-8 -*-

from django.contrib import admin

from assus_core.statistics.models import PosibleContagioORM


@admin.register(PosibleContagioORM)
class PosibleContagioAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'paciente',
        'posible_contagiado',
        'relacion',
        'lugar_contacto',
        'fecha_contacto',
    )
    raw_id_fields = (
        'paciente',
        'posible_contagiado',
    )
    search_fields = (
        'paciente__nombres',
        'paciente__ap_paterno',
        'paciente__ap_materno',
        'posible_contagiado__nombres',
        'posible_contagiado__apellidos',
    )
    list_filter = (
        'fecha_contacto',
    )
