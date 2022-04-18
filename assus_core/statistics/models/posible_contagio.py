# -*- coding: utf-8 -*-

from django.db import models
from assus_core.contrib.models import UUIDWithTimestampMixin


class PosibleContagioORM(UUIDWithTimestampMixin):
    paciente = models.ForeignKey(
        'PacienteORM',
        verbose_name='Paciente',
        on_delete=models.PROTECT,
    )
    posible_contagiado = models.ForeignKey(
        'PosibleContagiadoORM',
        verbose_name='Posible Contagiado',
        on_delete=models.PROTECT,
    )
    relacion = models.CharField(
        verbose_name='Relación',
        max_length=255,
    )
    lugar_contacto = models.CharField(
        verbose_name='Relación',
        max_length=255,
    )
    fecha_contacto = models.DateField(
        verbose_name='Fecha Contacto',
    )

    class Meta:
        db_table = 'posibles_contagios'
        verbose_name = 'Posible Contagio'
        verbose_name_plural = 'Posibles Contagios'
        ordering = ('-creacion', )
