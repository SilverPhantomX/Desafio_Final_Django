from django.shortcuts import render

# Create your views here.


def inicio(request):
    return render(request, 'paginas/inicio.html')

def Paqui(request):
    return render(request, 'paginas/Paquita.html')

def Inky(request):
    return render(request, 'paginas/Inky.html')

def Cirila(request):
    return render(request, 'paginas/Cirila.html')