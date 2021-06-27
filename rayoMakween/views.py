from django.http import response
from django.shortcuts import render
# importar las tablas para trabajar en la views
from .models import TipoTrabajo, Trabajo, Galeria, Contacto
# trabajar con la tabla de usuarios
from django.contrib.auth.models import User
# importar la libreria de autetificación
from django.contrib.auth import authenticate,logout,login as login_autent
#importar libreria de decoradores para autentificación
from django.contrib.auth.decorators import login_required,permission_required

#permite consumir servicios por medio de HTTP
import requests

# Create your views here.
def crear_usuario(request):
    if request.POST:
        nombre = request.POST.get("txtNombre")
        apellido = request.POST.get("txtApellido")
        email = request.POST.get("txtEmail")
        nom_usuario = request.POST.get("txtUsuario")
        pass1 = request.POST.get("txtPass1")
        pass2 = request.POST.get("txtPass2")

        if pass1!=pass2:
            contexto = {"mensaje":"las password no coinciden"}
            return render(request,"crear_usuario.html",contexto)

        usu = User()
        usu.first_name = nombre
        usu.last_name = apellido
        usu.email = email
        usu.username = nom_usuario
        usu.set_password(pass1)
        usu.save()

        contexto = {"mensaje":"grabo usuario"} 
        return render(request,"crear_usuario.html",contexto)

    return render(request,"crear_usuario.html")  

def index(request):
    lista = ["Electrónica Automotriz","Cajas de Cambio","Suspensión y Dirección"]
    trabajos = Trabajo.objects.filter(publicar=True).order_by('-nombre')[:3]
    variable = {"trabajos": trabajos,"nombre":"juanito","lista":lista}
    #consumir la api############################
    response = requests.get("http://127.0.0.1:8433/api/trabajos/")
    listado_trabajos = response.json()
    variable["listado_api"]=listado_trabajos
    ############################################
    return render(request, "index.html",variable)

def cerrar_sesion(request):
    logout(request)
    lista = ["Electrónica Automotriz","Cajas de Cambio","Suspensión y Dirección"]
    trabajos = Trabajo.objects.filter(publicar=True).order_by('-nombre')[:3]
    variable = {"trabajos": trabajos,"nombre":"juanito","lista":lista}
    return render(request,"index.html",variable)

def login(request):
    if request.POST:
        usuario = request.POST.get("txtNombre")
        password = request.POST.get("txtPass")
        us = authenticate(request,username=usuario, password=password)
        if us is not None and us.is_active:
            login_autent(request,us)  #almacenar usuario en request
            return render(request,"index.html")
        else:
            contexto = {"mensaje":"Usuario o Contraseña incorrecta"}
            return render(request,"login.html",contexto)    
    return render(request,"login.html") 

def filtro_tipo(request):
    trabajos = Trabajo.objects.filter(publicar=True)
    cant = Trabajo.objects.filter(publicar=True).count()
    tipos = TipoTrabajo.objects.all()
    if request.POST:
        tip = request.POST.get("cboTipo")
        obj_tipo = TipoTrabajo.objects.get(nombre=tip)
        trabajos = Trabajo.objects.filter(tipo=obj_tipo).filter(publicar=True)
        cant = Trabajo.objects.filter(tipo=obj_tipo).filter(publicar=True).count()
    contexto = {"trabajos":trabajos,"tipos":tipos,"cantidad":cant}
    return render(request, "galeria.html",contexto)

def filtro_tipo_boton(request, id):
    tipos = TipoTrabajo.objects.all()
    obj_tipo = TipoTrabajo.objects.get(nombre=id)
    trabajos = Trabajo.objects.filter(tipo=obj_tipo).filter(publicar=True)
    cant = Trabajo.objects.filter(tipo=obj_tipo).filter(publicar=True).count()
    contexto = {"trabajos":trabajos,"tipos":tipos,"cantidad":cant}
    return render(request, "galeria.html",contexto)    

def filtro_mecanico(request):
    trabajos = Trabajo.objects.all()
    tipos = TipoTrabajo.objects.all()
    if request.POST:
        texto = request.POST.get("txtTexto")
        trabajos = Trabajo.objects.filter(mecanico__contains=texto).filter(publicar=True)
    contexto = {"trabajos":trabajos,"tipos":tipos}
    return render(request, "galeria.html",contexto)

def galeria(request):
    trabajos = Trabajo.objects.filter(publicar=True)
    tipos = TipoTrabajo.objects.all()
    contexto = {"trabajos":trabajos,"tipos":tipos}
    return render(request, "galeria.html",contexto)

def detalle_trabajo(request, id):
    tra = Trabajo.objects.get(nombre=id)
    contexto = {"trabajo":tra}
    galeria_img = Galeria.objects.filter(trabajo=tra)
    contexto["galeria"] = galeria_img
    cantidad = Galeria.objects.filter(trabajo=tra).count()
    contexto["cantidad"] = cantidad
    return render(request,"ficha.html", contexto)

def info_trabajo(request, id):
    tra = Trabajo.objects.get(nombre=id)
    contexto = {"trabajo":tra}
    galeria_img = Galeria.objects.filter(trabajo=tra)
    contexto["galeria"] = galeria_img
    cantidad = Galeria.objects.filter(trabajo=tra).count()
    contexto["cantidad"] = cantidad
    return render(request,"info_trabajo.html", contexto)

def contacto(request):
    if request.POST:
        nombre = request.POST.get("txtNombre")
        correo = request.POST.get("txtCorreo")
        telefono = request.POST.get("txtFono")
        mensaje = request.POST.get("txtMens")

        con = Contacto(
            nombre=nombre,
            correo=correo,
            telefono=telefono,
            mensaje=mensaje 
        )
        con.save()
        return render(request,"contacto.html",{"comentario":"Enviado"})
    return render(request,"contacto.html")    

@login_required(login_url='/login/')
@permission_required('rayoMakween.delete_trabajo',login_url='/login/')
def eliminar_trabajo(request,id):
    nom_user = request.user.username
    try:
        tra = Trabajo.objects.get(nombre=id)
        tra.delete()
        mensaje = "Elimino Trabajo"
    except:
        mensaje = "No se encontro trabajo"
    tipos = TipoTrabajo.objects.all()
    trabajos = Trabajo.objects.filter(usuario=nom_user)
    contexto = {"mensaje":mensaje,"tipos":tipos,"trabajos":trabajos}
    return render(request,"registro.html",contexto) 

@login_required(login_url='/login/')
@permission_required('rayoMakween.view_trabajo',login_url='/login/')
def buscar(request, id):
    try:
        tra = Trabajo.objects.get(nombre=id)
        tipos = TipoTrabajo.objects.all()
        contexto = {"trabajo":tra,"tipos":tipos}
        return render(request,"modificar.html",contexto)
    except:
        mensaje = "No encontro trabajo"
    tipos = TipoTrabajo.objects.all()
    trabajos = Trabajo.objects.all()
    contexto = {"mensaje":mensaje,"tipos":tipos,"trabajos":trabajos}
    return render(request,"registro.html",contexto) 

@login_required(login_url='/login/')
@permission_required('rayoMakween.add_trabajo',login_url='/login/')
def registro(request):
    nom_user = request.user.username # recuperar nombre del usuario
    mensaje=""
    if request.POST:
        nombre = request.POST.get("txtNombre")
        try:
            t = Trabajo.objects.get(nombre=nombre)
            mensaje="Trabajo ya existe"
        except:  
            diagnostico = request.POST.get("txtDiagnostico") 
            fecha = request.POST.get("txtFecha")
            materiales= request.POST.get("txtMateriales")
            mecanico = nom_user
            imagen = request.FILES.get("txtImg")
            tipo = request.POST.get("cboTipo")
            # registro asociado al nombre de tipo trabajo
            obj_tipoTrabajo = TipoTrabajo.objects.get(nombre=tipo)
            tra = Trabajo()
            tra.nombre = nombre
            tra.diagnostico = diagnostico
            tra.fecha = fecha
            tra.materiales = materiales
            tra.mecanico = mecanico
            tra.tipo = obj_tipoTrabajo 
            tra.usuario = nom_user
            if imagen is not None:
                tra.imagen = imagen
            tra.save()
            mensaje="grabo"

    tipos = TipoTrabajo.objects.all()
    trabajos = Trabajo.objects.filter(usuario=nom_user)      
    cant = Trabajo.objects.filter(usuario=nom_user).count()
    contexto={"tipos":tipos,"trabajos":trabajos,"mensaje":mensaje,"cant":cant}
    return render(request,"registro.html",contexto)   

@login_required(login_url='/login/')
@permission_required('rayoMakween.change_trabajo',login_url='/login/')
def registro_modificar(request):
    nom_user = request.user.username
    mensaje=""
    if request.POST:
        nombre = request.POST.get("txtNombre")
        diagnostico = request.POST.get("txtDiagnostico") 
        fecha = request.POST.get("txtFecha")
        materiales= request.POST.get("txtMateriales")
        mecanico = request.POST.get("txtMecanico")
        tipo = request.POST.get("cboTipo") 
        obj_tipoTrabajo = TipoTrabajo.objects.get(nombre=tipo)
        try:
            t = Trabajo.objects.get(nombre=nombre)

            imagen = request.FILES.get("txtImg")

            if imagen is None:
                t.diagnostico=diagnostico
                t.fecha=fecha
                t.materiales=materiales
                t.mecanico=mecanico
                t.tipo=obj_tipoTrabajo
                t.comentario='--' 
                t.save()
                mensaje="modifico"
            else:    
                t.diagnostico=diagnostico
                t.fecha=fecha
                t.materiales=materiales
                t.mecanico=mecanico
                t.tipo=obj_tipoTrabajo
                t.imagen=imagen
                t.comentario='--' 
                t.save()
        except: 
            mensaje="No se puede modificar" 
    
    tipos = TipoTrabajo.objects.all()
    trabajos = Trabajo.objects.filter(usuario=nom_user)

    contexto={"tipos":tipos,"trabajos":trabajos,"mensaje":mensaje}
    return render(request,"registro.html",contexto) 

@login_required(login_url='/login/')
def insertar_imagen(request):
    mensaje=""
    if request.POST:
        nombre_trabajo = request.POST.get("txtTrabajo")
        imagen_trabajo = request.FILES.get("txtImg")
        obj_trabajo = Trabajo.objects.get(nombre=nombre_trabajo)

        if imagen_trabajo is not None:
            gale = Galeria()
            gale.imagen = imagen_trabajo
            gale.trabajo = obj_trabajo
            gale.save()
            mensaje = "Grabo Imagen"
        else:
            mensaje="no hay imagen para el trabajo"+nombre_trabajo

    nom_user = request.user.username    
    tipos = TipoTrabajo.objects.all()
    trabajos = Trabajo.objects.filter(usuario=nom_user)      
    contexto={"tipos":tipos,"trabajos":trabajos,"mensaje":mensaje}
    return render(request,"registro.html",contexto)     

