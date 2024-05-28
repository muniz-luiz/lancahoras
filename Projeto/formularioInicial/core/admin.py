from django.contrib import admin
from .models import Cliente, TipoCliente, Categoria, HorasCliente


admin.site.register(Cliente)
admin.site.register(TipoCliente)
admin.site.register(Categoria)
@admin.register(HorasCliente)
class HorasClienteAdmin(admin.ModelAdmin):
  list_display = ('id', 'cliente', 'tipo', 'Categoria', 'dataCliente')
  search_fields = ['Categoria__nomeCategoria']
  list_filter = ['tipo__nomeTipo']