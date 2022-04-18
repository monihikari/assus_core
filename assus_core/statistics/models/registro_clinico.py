# -*- coding: utf-8 -*-

from django.db import models

from assus_core.contrib.models import UUIDWithTimestampMixin
from assus_core.statistics.enums import EstadoPaciente


class RegistroClinicoORM(UUIDWithTimestampMixin):
    paciente = models.ForeignKey(
        'PacienteORM',
        verbose_name='Paciente',
        on_delete=models.PROTECT,
    )
    es_sintomatico = models.BooleanField(
        verbose_name='Es Sintomatico',
        default=False,
    )
    fecha_inicio_intomas = models.DateField(
        verbose_name='Fecha Inicio Sintomas',
        blank=True, null=True,
    )
    tiene_tos_seca = models.BooleanField(
        verbose_name='Tiene Tos Seca',
        default=False,
    )
    tiene_fiebre = models.BooleanField(
        verbose_name='Tiene Fiebre',
        default=False,
    )
    tiene_malestar_gral = models.BooleanField(
        verbose_name='Tiene Malestar Gral',
        default=False,
    )
    tiene_cefalea = models.BooleanField(
        verbose_name='Tiene Cefalea',
        default=False,
    )
    tiene_dificultar_respiratoria = models.BooleanField(
        verbose_name='Tiene Dificultar Respiratoria',
        default=False,
    )
    tiene_mialgias = models.BooleanField(
        verbose_name='Tiene Mialgias',
        default=False,
    )
    tiene_dolor_garganta = models.BooleanField(
        verbose_name='Tiene Dolor de Garganta',
        default=False,
    )
    tiene_dismunucion_olfato = models.BooleanField(
        verbose_name='Tiene perdida/disminucion del Olfato',
        default=False,
    )
    tiene_dismunucion_gusto = models.BooleanField(
        verbose_name='Tiene perdida/disminucion del Gusto',
        default=False,
    )
    otro_sintoma = models.TextField(
        verbose_name='Otro Sintoma',
        blank=True, null=True,
    )
    estado_paciente = models.CharField(
        default=EstadoPaciente.LEVE.value,
        verbose_name='Estado del Paciente',
        choices=EstadoPaciente.choices(),
        max_length=25,
    )
    fecha_defuncion = models.DateField(
        verbose_name='Fecha Defuncion',
        blank=True, null=True,
    )
    diag_sindrome_gripal = models.BooleanField(
        verbose_name='Diag. Sindrome Gripal',
        default=False,
    )
    diag_neumonia = models.BooleanField(
        verbose_name='Diag. Neumonia',
        default=False,
    )
    otro_diagnostico = models.TextField(
        verbose_name='Otro Diagnostico',
        blank=True, null=True,
    )

    def __str__(self):
        return f'{self.uuid}'

    class Meta:
        db_table = 'registros_clinicos'
        verbose_name = 'Registro Clinico'
        verbose_name_plural = 'Registro Clinicos'
        ordering = ('-creacion', )
