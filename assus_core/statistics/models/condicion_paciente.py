# -*- coding: utf-8 -*-

from django.db import models
from assus_core.contrib.models import UUIDWithTimestampMixin


class CondicionPacienteORM(UUIDWithTimestampMixin):
    paciente = models.ForeignKey(
        'PacienteORM',
        verbose_name='Paciente',
        on_delete=models.PROTECT,
    )
    tiene_hipertension = models.BooleanField(
        verbose_name='Tiene Hipertension Arterial',
        default=False,
    )
    tiene_obesisdad = models.BooleanField(
        verbose_name='Tiene Obesidad',
        default=False,
    )
    tiene_diabetes = models.BooleanField(
        verbose_name='Tiene Diabetes',
        default=False,
    )
    esta_embarazada = models.BooleanField(
        verbose_name='Esta embarazada',
        default=False,
    )
    tiene_enfermedad_oncologica = models.BooleanField(
        verbose_name='Tiene Enfermedad Oncológica',
        default=False,
    )
    tiene_enfermedad_cardiaca = models.BooleanField(
        verbose_name='Tiene Enfermedad Cardiaca',
        default=False,
    )
    tiene_enfermedad_respiratoria = models.BooleanField(
        verbose_name='Tiene Enfermedad Respiratoria',
        default=False,
    )
    tiene_enfermedad_renal = models.BooleanField(
        verbose_name='Tiene Enfermedad Renal',
        default=False,
    )
    otra_enfermedad = models.TextField(
        verbose_name='Tiene otra Enfermedad',
        blank=True, null=True,
    )

    def __str__(self):
        return f'{self.uuid}'

    class Meta:
        db_table = 'condicion_pacientes'
        verbose_name = 'Condicion de Paciente'
        verbose_name_plural = 'Condiciones de Pacientes'
        ordering = ('-creacion', )
