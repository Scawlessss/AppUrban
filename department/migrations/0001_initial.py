# Generated by Django 4.2.7 on 2023-12-04 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Deparment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "deparment_name",
                    models.CharField(
                        blank=True,
                        default="N/A",
                        max_length=240,
                        null=True,
                        verbose_name="Departamento",
                    ),
                ),
                (
                    "state",
                    models.CharField(
                        blank=True,
                        default="Activo",
                        max_length=100,
                        null=True,
                        verbose_name="Estado",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha Creación"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Fecha Actualización"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Departamento",
                "verbose_name_plural": "Departamentos",
                "ordering": ["deparment_name"],
            },
        ),
    ]
