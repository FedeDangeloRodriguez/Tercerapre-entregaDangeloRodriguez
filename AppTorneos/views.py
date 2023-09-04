from django.shortcuts import render
from django.http import HttpRequest
from .forms import *
from .models import *

# Create your views here.

def inicio(req):
    
    return render(req,"inicio.html",{"mensaje": "Bienvenido a mi primer Proyecto","saludo":"¡¡¡ Bienvenid@s !!!"})

def equipos(req):
    
    contexto = Equipo.objects.all()

    return render(req,"equipos.html", {"equipos": contexto})

def jugadores(req):
    
    contexto = Jugador.objects.all()

    return render(req,"jugadores.html", {"jugadores": contexto})

def entrenadores(req):
    
    contexto = Entrenadores.objects.all()

    return render(req,"entrenadores.html", {"entrenadores": contexto})

def equipo_formulario(req: HttpRequest):

    if req.method == "POST":

        miFormulario = EquipoFormulario(req.POST)

        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            equipo = Equipo(nombre=info['nombre'],barrio=info['barrio'],titulos=info['titulos'])
            equipo.save()
            return render(req,"inicio.html",{'mensaje': "Equipo creado!"})
        else:
            return render(req,"inicio.html",{'mensaje': "Formulario inválido."})
    else:
        miFormulario = EquipoFormulario()

        return render(req,"equipoFormulario.html",{"miFormulario":miFormulario})

def jugador_formulario(req: HttpRequest):

    if req.method == "POST":

        miFormulario = JugadorFormulario(req.POST)

        if miFormulario.is_valid():
            
            info = miFormulario.cleaned_data
            jugador = Jugador(nombre=info['nombre'],apellido=info['apellido'],edad=info['edad'])
            jugador.save()
            return render(req,"inicio.html",{'mensaje': "Jugador creado!"})
        else:
            return render(req,"inicio.html",{'mensaje': "Formulario inválido."})
    else:
        
        miFormulario = JugadorFormulario()
        return render(req,"jugadorFormulario.html",{"miFormulario":miFormulario})
    
def entrenador_formulario(req: HttpRequest):

    if req.method == "POST":
        miFormulario = EntrenadoresFormulario(req.POST)

        if miFormulario.is_valid():
            
            info = miFormulario.cleaned_data
            entrenador = Entrenadores(nombre=info['nombre'],apellido=info['apellido'],edad=info['edad'],titulos=info["titulos"])
            entrenador.save()
            return render(req,"inicio.html",{'mensaje': "Entrenador creado!"})
        else:
            return render(req,"inicio.html",{'mensaje': "Formulario inválido."})
    else:
        
        miFormulario = EntrenadoresFormulario()
        return render(req,"entrenadorFormulario.html",{"miFormulario":miFormulario})
    
def busqueda_equipo(req):

    return render(req,"BusquedaEquipo.html")

def buscar_equipo(req: HttpRequest):

    if req.GET["nombre"]:
        nombre = req.GET["nombre"]
        equipos = Equipo.objects.filter(nombre__icontains = nombre)
        if equipos:
            return render(req,"resulbusqueEquipo.html",{"equipos":equipos})
        else:
            return render(req,"inicio.html", {"mensaje":"No existe ese equipo."})
    else:
        return render(req,"inicio.html", {"mensaje":"No existe ese equipo."})
    
def busqueda_jugadores(req):

    return render(req,"BusquedaJugadores.html")

def buscar_jugadores(req: HttpRequest):

    if req.GET["nombre"]:
        nombre = req.GET["nombre"]
        jugadores = Jugador.objects.filter(nombre__icontains = nombre)
        if jugadores:
            return render(req,"resulbusqueJugador.html",{"jugadores":jugadores})
        else:
            return render(req,"inicio.html", {"mensaje":"No existe ese jugador."})
    else:
        return render(req,"inicio.html", {"mensaje":"No existe ese jugador."})
    
def busqueda_entrenador(req):

    return render(req,"BusquedaEntrenador.html")

def buscar_entrenador(req: HttpRequest):

    if req.GET["nombre"]:
        nombre = req.GET["nombre"]
        entrenadores = Entrenadores.objects.filter(nombre__icontains = nombre)
        if entrenadores:
            return render(req,"resulbusqueEntrenador.html",{"entrenadores":entrenadores})
        else:
            return render(req,"inicio.html", {"mensaje":"No existe ese entrenador."})
    else:
        return render(req,"inicio.html", {"mensaje":"No existe ese entrenador."})

    
def elimina_jugadores(req: HttpRequest,id):

    if req.method == "POST":

        jugador = Jugador.objects.get(id=id)
        jugador.delete()

        jugadores = Jugador.objects.all()

        return render(req,"jugadores.html",{"jugadores":jugadores})
    
def elimina_entrenadores(req: HttpRequest,id):

    if req.method == "POST":

        entrenador = Entrenadores.objects.get(id=id)
        entrenador.delete()

        entrenadores = Entrenadores.objects.all()

        return render(req,"entrenadores.html",{"entrenadores":entrenadores})
    
def elimina_equipos(req: HttpRequest,id):

    if req.method == "POST":

        equipo = Equipo.objects.get(id=id)
        equipo.delete()

        equipos = Equipo.objects.all()

        return render(req,"equipos.html",{"equipos":equipos})