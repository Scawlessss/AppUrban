# Generated by Django 4.2.7 on 2023-11-27 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("incident", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Poll",
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
                    "name",
                    models.CharField(
                        blank=True,
                        default="N/A",
                        max_length=240,
                        null=True,
                        verbose_name="Incidente",
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
                    "incident",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="incident.incident",
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
                "verbose_name": "Encuesta",
                "verbose_name_plural": "Encuesta",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Fields",
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
                    "name",
                    models.CharField(
                        blank=True,
                        default="name",
                        max_length=240,
                        null=True,
                        verbose_name="name",
                    ),
                ),
                (
                    "label",
                    models.CharField(
                        blank=True,
                        default="Label",
                        max_length=240,
                        null=True,
                        verbose_name="Label",
                    ),
                ),
                (
                    "placeholder",
                    models.CharField(
                        blank=True,
                        default="placeholder",
                        max_length=240,
                        null=True,
                        verbose_name="Placeholder",
                    ),
                ),
                (
                    "kind",
                    models.CharField(
                        blank=True,
                        default="Tipo_campo",
                        max_length=240,
                        null=True,
                        verbose_name="Tipo_campo",
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
                    "poll",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="poll.poll"
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
                "verbose_name": "Campo",
                "verbose_name_plural": "Campo",
                "ordering": ["name"],
            },
        ),
    ]