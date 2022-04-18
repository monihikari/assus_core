# -*- coding: utf-8 -*-

from django.db import models
from assus_core.contrib.models import UUIDWithTimestampMixin


class FichaEpidemiologicaORM(UUIDWithTimestampMixin):
    estblecimiento = models.ForeignKey(
        'EstablecimientoORM',
        verbose_name='Estblecimiento de Salud',
        on_delete=models.PROTECT,
    )
    paciente = models.ForeignKey(
        'PacienteORM',
        verbose_name='Paciente',
        on_delete=models.PROTECT,
    )
    antecedente = models.ForeignKey(
        'AntecedenteORM',
        verbose_name='Antecedente',
        on_delete=models.PROTECT,
    )
    registro_clinico = models.ForeignKey(
        'RegistroClinicoORM',
        verbose_name='Registro Clinico',
        on_delete=models.PROTECT,
    )
    hospitalizacion = models.ForeignKey(
        'HospitalizacionORM',
        verbose_name='Hospitalización',
        on_delete=models.SET_NULL,
        blank=True, null=True,
    )
    condicion_paciente = models.ForeignKey(
        'CondicionPacienteORM',
        verbose_name='Condicion Paciente',
        on_delete=models.PROTECT,
    )
    posibles_contagios = models.ManyToManyField(
        'PosibleContagioORM',
        verbose_name='Posibles Contagios',
        blank=True,
    )
    registro_laboratorio = models.ForeignKey(
        'RegistroLaboratorioORM',
        verbose_name='Registro Laboratorio',
        on_delete=models.PROTECT,
    )
    nombres_notificador = models.CharField(
        verbose_name='Nombres (Notificador)',
        max_length=255,
    )
    apellidos_notificador = models.CharField(
        verbose_name='Apellidos (Notificador)',
        max_length=255,
    )
    telefonno_notificador = models.CharField(
        verbose_name='Telefono (Notificador)',
        max_length=255,
        blank=True, null=True,
    )
    fecha_notificacion = models.DateField(
        verbose_name='Fecha de Notificacion',
        blank=True, null=True,
    )
    semana_epidemiologica = models.PositiveIntegerField(
        verbose_name='Semana Epidemiologica',
        blank=True, null=True,
    )
    identificado_en_busqueda_activa = models.BooleanField(
        verbose_name='Identificado en Busqueda Activa',
        default=False,
    )

    def __str__(self):
        return f'{self.uuid}'

    class Meta:
        db_table = 'fichas_epidemiologicas'
        verbose_name = 'Ficha Epidemiologica'
        verbose_name_plural = 'Ficha Epidemiologicas'
        ordering = ('-creacion', )
