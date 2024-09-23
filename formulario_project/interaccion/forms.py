from django import forms

class FormularioCompleto(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    opciones = forms.ChoiceField(label='Selecciona una opción', choices=[
        ('opcion1', 'Opción 1'),
        ('opcion2', 'Opción 2'),
        ('opcion3', 'Opción 3'),
    ])
    comentarios = forms.CharField(label='Comentarios', widget=forms.Textarea)
