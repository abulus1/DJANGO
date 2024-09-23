from django.shortcuts import render
from .forms import FormularioCompleto

def saludo(request):
    if request.method == 'POST':
        form = FormularioCompleto(request.POST)
        if form.is_valid():
            # Aquí puedes manejar los datos del formulario
            # Por ejemplo, form.cleaned_data['nombre'] para obtener el nombre
            pass
    else:
        form = FormularioCompleto()
    
    return render(request, 'interaccion/formulario.html', {'form': form})
