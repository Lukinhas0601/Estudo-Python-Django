from django.shortcuts import render
from eventos.models import Certificados

# Create your views here.
def meus_certificados(request):
    certificados = Certificados.objects.filter(participante=request.user)
    return render(request, 'meus_certificados.html', {'certificados':certificados})
