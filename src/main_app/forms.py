from django import forms


class TareaForm(forms.Form):
    nombre = forms.CharField(label = 'Nombre',max_length = 50)
    descripcion = forms.CharField(label = 'Descripcion',max_length = 50)
    inicio = forms.DateTimeField(
        label = 'Inicio',
        widget=forms.Select(attrs={'class': "dropdown-button"}),
    )
    termino = forms.DateTimeField(label = 'Termino')
   
    TERMINADA = 'terminada'
    PENDIENTE = 'pendiente'
    CANCELADA = 'cancelada'
    LIMITE = 'limite'
    ESTADOS_TAREAS = (
        (TERMINADA, 'Terminada'),
        (PENDIENTE, 'Pendiente'),
        (CANCELADA, 'Cancelada'),
        (LIMITE, 'Limite'),
    )
    img = forms.CharField(label = 'Imagen', max_length=255)
    estado = forms.ChoiceField(label = 'Estado',
        choices = ESTADOS_TAREAS,
        widget=forms.Select(attrs={'class': "dropdown-button"}),
        
    )
    

    
