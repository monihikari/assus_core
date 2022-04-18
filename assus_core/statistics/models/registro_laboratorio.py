# -*- coding: utf-8 -*-

from django.db import models

from assus_core.contrib.models import UUIDWithTimestampMixin
from assus_core.statistics.enums import (
    RazonRechazoLaboratorio,
    TipoMuestra,
    MetodoDiagnostico,
    ResultadoLaboratorio,
)


class RegistroLaboratorioORM(UUIDWithTimestampMixin):
    paciente = models.ForeignKey(
        'PacienteORM',
        verbose_name='Paciente',
        on_delete=models.PROTECT,
    )
    se_tomo_muestra = models.BooleanField(
        verbose_name='Se Tomó muestra para Lab.',
        default=False,
    )
    razon_rechazo = models.CharField(
        verbose_name='Razon Rechazo',
        choices=RazonRechazoLaboratorio.choices(),
        max_length=50,
        blank=True, null=True,
    )
    otra_razon_rechazo = models.TextField(
        verbose_name='Otra Razon de rechazo',
        blank=True, null=True,
    )
    tipo_muestra = models.CharField(
        verbose_name='Tipo de Muestra',
        choices=TipoMuestra.choices(),
        max_length=50,
        blank=True, null=True,
    )
    otro_tipo_muestra = models.TextField(
        verbose_name='Otro Tipo de Muestra',
        blank=True, null=True,
    )
    laboratorio_procesador = models.TextField(
        verbose_name='Nombre Laboratorio',
        help_text='Es el Laboratorio que procesará la muestra',
        blank=True, null=True,
    )
    fecha_toma_muestra = models.DateField(
        verbose_name='Fecha Toma de Muestra',
        blank=True, null=True,
    )
    fecha_envio_muestra = models.DateField(
        verbose_name='Fecha Envio de Muestra',
        blank=True, null=True,
    )
    observaciones = models.TextField(
        verbose_name='Observaciones',
        blank=True, null=True,
    )
    metodo_diagnostico = models.CharField(
        verbose_name='Método de Diagnostico',
        choices=MetodoDiagnostico.choices(),
        max_length=50,
        blank=True,
        null=True,
    )
    resultado = models.CharField(
        verbose_name='Resultado',
        choices=ResultadoLaboratorio.choices(),
        max_length=50,
        blank=True,
        null=True,
    )
    fecha_resultado = models.DateField(
        verbose_name='Fecha del Resultado',
        blank=True, null=True,
    )

    def __str__(self):
        return f'{self.uuid}'

    class Meta:
        db_table = 'registros_laboratorio'
        verbose_name = 'Registro de Laboratorio'
        verbose_name_plural = 'Registros de Laboratorio'
        ordering = ('-creacion', )
