from django.http import HttpResponse
from django.shortcuts import render
from .models import HorasCliente

def cadastroHoras(request):
  if request.method == 'POST':
    cliente = request.POST.get('cliente')
    categoria = request.POST.get('categoria')
    tipo = request.POST.get('tipo')
    data = request.POST.get('data')
    horainicio = request.POST.get('horainicio')
    horafim = request.POST.get('horafim')    

    return HttpResponse('informação salva com sucesso')
  return render(request, 'cadastro/form.html')

