# -*- coding: utf-8 -*-

from django.db import models

from assus_core.contrib.models import UUIDWithTimestampMixin


class HospitalizacionORM(UUIDWithTimestampMixin):
    paciente = models.ForeignKey(
        'PacienteORM',
        verbose_name='Paciente',
        on_delete=models.PROTECT,
    )
    estblecimiento = models.ForeignKey(
        'EstablecimientoORM',
        verbose_name='Estblecimiento de Salud',
        on_delete=models.PROTECT,
    )
    es_ambulatorio = models.BooleanField(
        verbose_name='Es Ambulatorio',
        default=False,
    )
    es_internado = models.BooleanField(
        verbose_name='Es Internado',
        default=False,
    )
    lugar_aislamiento = models.TextField(
        verbose_name='Lugar Aislamiento',
        blank=True, null=True,
    )
    fecha_aislamiento = models.DateField(
        verbose_name='Fecha Aislamiento',
        blank=True, null=True,
    )
    fecha_internacion = models.DateField(
        verbose_name='Fecha Internacion',
        blank=True, null=True,
    )
    con_ventilacion_mecanica = models.BooleanField(
        verbose_name='Con Ventilación Mecanica',
        default=False,
    )
    es_terapia_intensiva = models.BooleanField(
        verbose_name='En Terapia INtensiva',
        default=False,
    )
    fecha_ingreso_uti = models.DateField(
        verbose_name='Fecha de Ingreso(UTI)',
        blank=True, null=True,
    )

    def __str__(self):
        return f'{self.uuid}'

    class Meta:
        db_table = 'hospitalizaciones'
        verbose_name = 'Hospitalizacion'
        verbose_name_plural = 'Hospitalizaciones'
        ordering = ('-creacion', )
