# -*- coding: utf-8 -*-

from django.db import models
from assus_core.contrib.models import UUIDWithTimestampMixin
from assus_core.statistics.models.paciente import Genero


class PosibleContagiadoORM(UUIDWithTimestampMixin):
    nombres = models.CharField(
        verbose_name='Nombres',
        max_length=255,
    )
    apellidos = models.CharField(
        verbose_name='Apellidos',
        max_length=255,
    )
    genero = models.CharField(
        verbose_name='Género',
        max_length=2,
        choices=Genero.choices(),
    )
    telefono = models.CharField(
        verbose_name='Teléfono',
        max_length=255,
        blank=True, null=True,
    )
    direccion = models.TextField(
        verbose_name='direccion',
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

    class Meta:
        db_table = 'posibles_contagiados'
        verbose_name = 'Posible Contagiado'
        verbose_name_plural = 'Posibles Contagiados'
        ordering = ('-creacion', )
