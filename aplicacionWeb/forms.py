from django import forms
from aplicacionWeb.models import Contacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



from django import forms
from aplicacionWeb.models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_de_boleta': forms.TextInput(attrs={'class': 'form-control'}),

        }
    OPCIONES_RESOLUCION = [('cambio', 'Cambio'), ('devolucion', 'Devolucion')]
    OPCIONES_MOTOCICLETAS = [
    ('Y-FZ25', 'Yamaha FZ25'), ('Y-FZ150', 'Yahama FZ150'),
    ('Y-MT03', 'Yamaha MT03'), ('Y-NMAX', 'Yamaha NMax'),
    ('Y-R3', 'Yamaha R3'), ('Y-R7', 'Yamaha R7'),
    ('Y-R15', 'Yamaha R15'), ('Y-T9', 'Yamaha Tracer 9')
]

    OPCIONES_COMPRA = [('efectivo', 'Efectivo'), ('tarjeta', 'Tarjeta')]
    OPCIONES_COMUNA = [('cerrillos', 'Cerrillos'), ('cerro-navia', 'Cerro Navia'),
                       ('conchali', 'Conchalí'), ('el-bosque', 'El Bosque'),
                       ('estacion-central', 'Estación Central'), ('huechuraba', 'Huechuraba'),
                       ('independencia', 'Independencia'), ('la-cisterna', 'La Cisterna'),
                       ('la-florida', 'La Florida'), ('la-granja', 'La Granja'),
                       ('la-pintana', 'La Pintana'), ('la-reina', 'La Reina'),
                       ('las-condes', 'Las Condes'), ('lo-barnechea', 'Lo Barnechea'),
                       ('lo-espejo', 'Lo Espejo'), ('lo-prado', 'Lo Prado'),
                       ('macul', 'Macul'), ('maipu', 'Maipú'), ('ñuñoa', 'Ñuñoa'),
                       ('pedro-aguirre-cerda', 'Pedro Aguirre Cerda'), ('peñalolen', 'Peñalolen'),
                       ('providencia', 'Providencia'), ('pudahuel', 'Pudahuel'),
                       ('quilicura', 'Quilicura'), ('quinta-normal', 'Quinta Normal'),
                       ('recoleta', 'Recoleta'), ('renca', 'Renca'), ('san-joaquin', 'San Joaquín'),
                       ('san-miguel', 'San Miguel'), ('san-ramon', 'San Ramón'),
                       ('santiago-centro', 'Santiago Centro'), ('vitacura', 'Vitacura')]

    comuna = forms.CharField(widget=forms.Select(choices=OPCIONES_COMUNA, attrs={'class': 'form-control'}))
    medio_de_compra = forms.CharField(widget=forms.Select(choices=OPCIONES_COMPRA, attrs={'class': 'form-control'}))
    cambio_o_devolucion = forms.CharField(widget=forms.Select(choices=OPCIONES_RESOLUCION, attrs={'class': 'form-control'}))
    comentarios = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    producto = forms.ChoiceField(
    widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-multiple'}),
    choices=OPCIONES_MOTOCICLETAS
)

class CustomUserCreationForm(UserCreationForm):
    # Clase de formulario personalizado que hereda de UserCreationForm

    class Meta:
        # La clase Meta proporciona metadatos adicionales para el formulario
        model = User  # Especifica el modelo de usuario asociado al formulario
        fields = ['username', 'email', 'password1', 'password2']  
        # Especifica los campos que se mostrarán en el formulario y su orden

    # Puedes añadir métodos adicionales o personalizaciones del formulario aquí si es necesario
