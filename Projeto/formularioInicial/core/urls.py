from django.urls import path

from .views import cadastroHoras

urlpatterns = [
  path('cadastro/', cadastroHoras, name = 'cadastro')
]