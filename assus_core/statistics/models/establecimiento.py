# -*- coding: utf-8 -*-

from django.db import models

from assus_core.contrib.models import UUIDWithTimestampMixin
from assus_core.statistics.enums import SubSector


class EstablecimientoORM(UUIDWithTimestampMixin):
    nombre = models.CharField(
        verbose_name='Nombre',
        max_length=255,
    )
    cod_establecimiento = models.CharField(
        verbose_name='Cód. Establecimiento',
        max_length=255,
        blank=True, null=True,
    )
    red_salud = models.CharField(
        verbose_name='Red de Salud',
        max_length=255,
        blank=True, null=True,
    )
    sub_sector = models.CharField(
        verbose_name='Sub Sector',
        choices=SubSector.choices(),
        max_length=50,
        blank=True, null=True,
    )
    otro_sub_sector = models.CharField(
        verbose_name='Otro Sub Sector',
        max_length=255,
    )
    direccion = models.ForeignKey(
        'DireccionORM',
        verbose_name='Dirección',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        db_table = 'establecimientos'
        verbose_name = 'Establecimiento'
        verbose_name_plural = 'Establecimientos'
        ordering = ('-creacion', )
