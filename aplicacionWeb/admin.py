from django.contrib import admin
from aplicacionWeb.models import Motocicletas, Contacto


class MotocicletasAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','precio']
    

class ContactoAdmin(admin.ModelAdmin):
    list_display = ['id_contacto','nombre','correo','telefono','direccion','comuna','producto','numero_de_boleta','medio_de_compra','cambio_o_devolucion','comentarios']

admin.site.register(Motocicletas,MotocicletasAdmin)
admin.site.register(Contacto,ContactoAdmin)
