from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q
from .forms import *
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegistroForm
from .models import UsuarioLogin, Jugador
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import  login
from datetime import datetime


def index(request):
    if(not "fecha_inicio" in request.session):
        request.session["fecha_inicio"] = datetime.now().strftime('%d/%m/%Y %H:%M')
    return render(request, 'index.html')

def borrar_session(request):
    del request.session['fecha_inicio']
    return render(request, 'index.html')





#Distintos errores de las paginas web
def mi_error_404(request, exception=None):
    return render(request, 'torneo/errores/404.html', None,None,404)
def mi_error_400(request, exception=None):
    return render(request, 'torneo/errores/400.html', None,None,400)
def mi_error_403(request, exception=None):
    return render(request, 'torneo/errores/403.html', None,None,403)
def mi_error_500(request, exception=None):
    return render(request, 'torneo/errores/403.html', None,None,500)

