from django.utils import timezone
import datetime
from django.shortcuts import render
from django.http import Http404
from .models import Post

def post_list(request):
    posts = Post.objects.filter(fecha_creacion__lte=timezone.now())
    return render(request, 'modelos/post_list.html', {'Posts': posts})

def fecha_actual(request):
    ahora = datetime.datetime.now()
    return render(request, 'fecha_actual.html', {'fecha_actual': ahora})

def horas_adelante(request, horas):
    try:
        horas = int(horas)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=horas)
    return render(request, 'horas_adelante.html', {'hora_siguiente': dt, 'horas': horas })