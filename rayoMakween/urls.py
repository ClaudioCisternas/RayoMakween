from django.contrib import admin
from django.urls import path, include
from .views import index, galeria, registro, eliminar_trabajo, detalle_trabajo, filtro_tipo, filtro_mecanico, filtro_tipo_boton, login, cerrar_sesion, crear_usuario, buscar, registro_modificar, insertar_imagen, info_trabajo, contacto

urlpatterns = [
    path('',index,name='IND'),
    path('galeria/',galeria,name='GALE'),
    path('registro/',registro, name='REGI'),
    path('eliminar_trabajo/<id>/',eliminar_trabajo,name='ELIM'),
    path('detalle/<id>/', detalle_trabajo,name='DT'),
    path('filtro_tipo/',filtro_tipo,name='FILTROT'),
    path('filtro_meca/',filtro_mecanico,name='FILTROM'),
    path('filtro_tipo_trabajo/<id>/',filtro_tipo_boton,name='FILTROTT'),
    path('login/',login,name='LOGIN'),
    path('logout/',cerrar_sesion,name='CERRAR'),
    path('crear_usuario/',crear_usuario,name='CREARU'),
    path('buscar/<id>/',buscar,name='BUSCAR'),
    path('modificar/',registro_modificar,name='MODI'),
    path('insertar_imagen/',insertar_imagen,name='INSERTARIMG'),
    path('info_trabajo/<id>/',info_trabajo,name='INFOTRAB'),
    path('contacto/',contacto,name='CONT'),
]
