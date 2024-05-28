from django.db import models
import uuid

class Cliente(models.Model):
  id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
  nomeCliente = models.CharField(blank=False,max_length=255)
  def __str__(self) -> str:
    return self.nomeCliente.upper()

class TipoCliente(models.Model):
  id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
  nomeTipo = models.CharField(blank=False, max_length=255)
  def __str__(self) -> str:
    return self.nomeTipo.upper()

class Categoria(models.Model):
  id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
  nomeCategoria = models.CharField(blank=False, max_length=255)
  def __str__(self) -> str:
    return self.nomeCategoria.upper()
    

class HorasCliente(models.Model):
  id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
  cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
  tipo = models.ForeignKey(TipoCliente, on_delete=models.PROTECT)
  info = models.TextField(blank=False, max_length=1000)
  Categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
  dataCliente = models.DateField()
  horaInicio = models.TimeField()
  horaFim = models.TimeField()

  def __str__(self) -> str:
    return self.cliente.nomeCliente.upper()
  

  

  
