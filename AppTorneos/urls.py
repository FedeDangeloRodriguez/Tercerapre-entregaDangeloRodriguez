from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name= "Inicio"),
    path('equipos/', equipos, name= "Equipos" ),
    path('jugadores/', jugadores,name= "Jugadores" ),
    path('entrenadores/', entrenadores, name= "Entrenadores" ),
    path('equipo-formulario/', equipo_formulario,name= "EquipoFormulario" ),
    path('jugador-formulario/', jugador_formulario,name= "JugadorFormulario" ),
    path('entrenador-formulario/', entrenador_formulario,name= "EntrenadorFormulario" ),
    path('busqueda-equipo/', busqueda_equipo,name= "BusquedaEquipo" ),
    path('buscar/', buscar_equipo,name= "Buscar" ),
    path('busqueda-jugadores/', busqueda_jugadores,name= "BusquedaJugadores" ),
    path('buscar-jugadores/', buscar_jugadores,name= "BuscarJugadores" ),
    path('busqueda-entrenadores/', busqueda_entrenador,name= "BusquedaEntrenador" ),
    path('buscar-entrenadores/', buscar_entrenador,name= "BuscarEntrenadores" ),
    path('elimina-jugadores/<int:id>', elimina_jugadores,name= "EliminaJugadores" ),
    path('elimina-entrenadores/<int:id>', elimina_entrenadores,name= "EliminaEntrenadores" ),
    path('elimina-equipos/<int:id>', elimina_equipos,name= "EliminaEquipos" ),
]