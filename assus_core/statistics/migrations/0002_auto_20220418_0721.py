# Generated by Django 3.2.13 on 2022-04-18 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fichaepidemiologicaorm',
            name='estblecimiento',
        ),
        migrations.AddField(
            model_name='fichaepidemiologicaorm',
            name='establecimiento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='statistics.establecimientoorm', verbose_name='Establecimiento de Salud'),
            preserve_default=False,
        ),
    ]
