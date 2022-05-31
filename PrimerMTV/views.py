from django.shortcuts import render
from PrimerMTV.models import Familiares
# Create your views here.

def mostrarFamilia(request):
    #DESDE ACA SE HACE LA UNION CON LA BD PARA MOSTRARLOS 
    flia = Familiares.objects.all()
    Contexto= {'flia':flia}
    return render(request,'familia.html',Contexto)
    
    
