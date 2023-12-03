from django.db import models


class Motocicletas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return str(self.id)

    

class Contacto(models.Model):
    id_contacto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    correo = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=9)
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=50)
    producto = models.CharField(max_length=50)
    numero_de_boleta = models.CharField(max_length=10)
    medio_de_compra = models.CharField(max_length=15)
    cambio_o_devolucion = models.CharField(max_length=15)
    comentarios = models.CharField(max_length=100)


    def __str__(self):
        return self.nombre