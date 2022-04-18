# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _

from assus_core.contrib.enums import BaseEnum
from assus_core.contrib.models import UUIDWithTimestampMixin
from assus_core.contrib.time import TimeUtils


class TipoDocIdentidad(BaseEnum):
    CEDULA_IDENTIDAD = 'CEDULA_IDENTIDAD'
    PASAPORTE = 'PASAPORTE'
    CEDULA_EXTRANJERO = 'CEDULA_EXTRANJERO'


class Genero(BaseEnum):
    MASCULINO = 'M'
    FEMENINO = 'F'


class PacienteORM(UUIDWithTimestampMixin):
    doc_identidad = models.CharField(
        verbose_name=_('C.I.'),
        max_length=12,
    )
    tipo_doc_identidad = models.CharField(
        default=TipoDocIdentidad.CEDULA_IDENTIDAD.value,
        verbose_name='Tipo Doc. Identidad',
        choices=TipoDocIdentidad.choices(),
        max_length=25,
    )
    fecha_nacimiento = models.DateField(
        verbose_name='Fecha Nacimiento',
    )
    nombres = models.CharField(
        verbose_name='Nombres',
        max_length=255,
    )
    ap_paterno = models.CharField(
        verbose_name='Ap. Paterno',
        max_length=255,
    )
    ap_materno = models.CharField(
        verbose_name='Ap. Materno',
        max_length=255,
        blank=True,
        null=True
    )
    genero = models.CharField(
        verbose_name='Género',
        max_length=2,
        choices=Genero.choices(),
    )
    idendificacion_etnica = models.CharField(
        verbose_name='Identificación étnica',
        max_length=255,
        blank=True, null=True,
    )
    direccion = models.ForeignKey(
        'DireccionORM',
        verbose_name='Direccion',
        on_delete=models.SET_NULL,
        blank=True, null=True,
    )

    @property
    def edad(self) -> int:
        hoy = TimeUtils.utc_now().date()
        return (
            hoy.year - self.fecha_nacimiento.year - (
                (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
            )
        )

    def __str__(self):
        return f'{self.nombres} {self.ap_paterno} {self.ap_materno}'

    class Meta:
        db_table = 'pacientes'
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ('-creacion', )
