# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _

from assus_core.contrib.models import UUIDWithTimestampMixin
from assus_core.statistics.enums import TipoOcupacion


class AntecedenteORM(UUIDWithTimestampMixin):
    paciente = models.ForeignKey(
        'PacienteORM',
        verbose_name='Paciente',
        on_delete=models.PROTECT,
    )
    tipo_ocupacion = models.CharField(
        default=TipoOcupacion.CEDULA_IDENTIDAD.value,
        verbose_name='Tipo Doc. Identidad',
        choices=TipoOcupacion.choices(),
        blank=True, null=True,
        max_length=25,
    )
    ocupacion_otro = models.CharField(
        verbose_name=_('Ocupación (Otro)'),
        max_length=255,
    )
    lugar_probable_infeccion = models.ForeignKey(
        'DireccionORM',
        verbose_name='Lugar Probable Infección',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    contacto_covid = models.BooleanField(
        verbose_name='Contacto COVID',
        default=False,
    )
    fecha_contacto_covid = models.DateField(
        verbose_name='Fecha Contacto COVID',
        blank=True, null=True,
    )
    tuvo_covid = models.BooleanField(
        verbose_name='Tuvo COVID',
        default=False,
    )
    fecha_diagnostico_covid = models.DateField(
        verbose_name='Fecha Diagnostico COVID',
        blank=True, null=True,
    )

    def __str__(self):
        return f'{self.uuid}'

    class Meta:
        db_table = 'antecedentes'
        verbose_name = 'Antecedente'
        verbose_name_plural = 'Antecedentes'
        ordering = ('-creacion', )
