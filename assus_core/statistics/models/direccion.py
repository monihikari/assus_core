# -*- coding: utf-8 -*-

from django.db import models
from assus_core.contrib.models import UUIDWithTimestampMixin


class DireccionORM(UUIDWithTimestampMixin):
    pais = models.CharField(
        verbose_name='Pais',
        max_length=100,
        blank=True, null=True,
    )
    departamento = models.CharField(
        verbose_name='Departamento',
        max_length=255,
        blank=True, null=True,
    )
    municipio = models.CharField(
        verbose_name='Muicipio',
        max_length=255,
        blank=True, null=True,
    )
    ciudad = models.CharField(
        verbose_name='Ciudad/Localidad',
        max_length=255,
        blank=True, null=True,
    )
    calle = models.CharField(
        verbose_name='Calle',
        max_length=255,
        blank=True, null=True,
    )
    zona = models.CharField(
        verbose_name='Zona',
        max_length=255,
        blank=True, null=True,
    )
    telefono = models.CharField(
        verbose_name='Telefono',
        max_length=255,
        blank=True, null=True,
    )
    apoderado = models.CharField(
        verbose_name='Apoderado',
        max_length=255,
        blank=True, null=True,
    )

    def __str__(self):
        return f'{self.uuid}'

    class Meta:
        db_table = 'direcciones'
        verbose_name = 'Direccion'
        verbose_name_plural = 'Direcciones'
        ordering = ('-creacion', )
