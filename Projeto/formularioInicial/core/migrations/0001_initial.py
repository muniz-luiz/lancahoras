# Generated by Django 5.0.6 on 2024-05-24 16:53

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('nomeCategoria', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('nomeCliente', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('nomeTipo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HorasCliente',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('info', models.TextField(max_length=1000)),
                ('dataCliente', models.DateField()),
                ('horaInicio', models.TimeField()),
                ('horaFim', models.TimeField()),
                ('Categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.categoria')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.cliente')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.tipocliente')),
            ],
        ),
    ]
