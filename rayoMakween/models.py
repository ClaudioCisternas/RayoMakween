from django.db import models

# Create your models here.

class TipoTrabajo(models.Model):
    nombre = models.CharField(primary_key=True,max_length=45)

    def __str__(self):
        return self.nombre

class Trabajo(models.Model):
    nombre = models.CharField(primary_key=True,max_length=50)
    diagnostico = models.TextField()    
    fecha = models.DateField()
    materiales =  models.TextField()
    mecanico = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='trabajos',default='trabajos/defecto.jpg')
    publicar = models.BooleanField(default=False)
    comentario = models.TextField(default='--')
    usuario = models.CharField(null=True,max_length=45)
    tipo = models.ForeignKey(TipoTrabajo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Galeria(models.Model):
    auto_inc = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='galerias')
    trabajo = models.ForeignKey(Trabajo,on_delete=models.CASCADE)

    def __str__(self):
        return "Numero:" + str(self.auto_inc)  

class Contacto(models.Model):    
    nombre = models.CharField(primary_key=True,max_length=50)  
    correo = models.EmailField()
    telefono= models.CharField(max_length=10) 
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre