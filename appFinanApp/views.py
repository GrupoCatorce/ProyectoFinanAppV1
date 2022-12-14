from email import message
from re import template
from wsgiref.util import request_uri
from xml.dom.expatbuilder import DOCUMENT_NODE
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from ast import Delete
import json
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View

from .models import Administrador, Login, Perfil_Empresa


class AdministradorViews(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, User=0):
        if User > 0:
            adm = list(Administrador.objects.filter(UserID=User).values())
            if len(adm) > 0:
                respuesta = adm[0]
                datos = {"administrador": respuesta}
            else:
                datos = {"Respuesta": "No se encontrarton datos"}
        else:
            template_name = "consultarAdmon.html"
            adm = Administrador.objects.all()
            datos = {'listadoAdmon': adm}
        return render(request, template_name, datos)

    def post(self, request):

        Administrador.objects.create(UserID=request.POST["UserID"], Nombre=request.POST["Nombre"], Apellido=request.POST["Apellido"],
                                     Email=request.POST["Email"], Celular=request.POST["Celular"], Fecha_Ingreso_Empresa=request.POST["Fecha_Ingreso_Empresa"])
        return redirect('/Administrador/')

    def put(self, request, User):
        datos = json.loads(request.body)
        adm = list(Administrador.objects.filter(UserID=User).values())
        if len(adm) > 0:
            NewUser = Administrador.objects.get(UserID=User)
            NewUser.UserID = datos['UserID']
            NewUser.Nombre = datos['Nombre']
            NewUser.Apellido = datos['Apellido']
            NewUser.Email = datos['Email']
            NewUser.Celular = datos['Celular']
            NewUser.Fecha_Ingreso_Empresa = datos['Fecha de Ingreso Empresa']
            NewUser.save()
            mensaje = {"Respuesta": "Se actualizaron los datos correctamente"}
        else:
            mensaje = {"Respuesta": "No se encontraron datos"}
        return JsonResponse(mensaje)

    def delete(self, request, User):
        adm = list(Administrador.objects.filter(UserID=User).values())
        if len(adm) > 0:
            Administrador.objects.filter(UserID=User).delete
            mensaje = {"Respuesta": "El registro se elimino correctamente"}
        else:
            mensaje = {"Respuesta": "No se encontraron datos"}
        return JsonResponse(mensaje)

class OperarioViews(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, User=0):
        if User > 0:
            ope = list(Operario.objects.filter(UserID=User).values())
            if len(ope) > 0:
                respuesta = ope[0]
                datos = {"operario": respuesta}
            else:
                datos = {"Respuesta": "No se encontraron datos"}
        else:
            template_name = "consultarOpera.html"
            ope = Operario.objects.all()
            datos = {'listadoOpera': ope}
        return render(request, template_name, datos)

    def post(self, request):

        Operario.objects.create(UserID=request.POST["UserID"], Nombre=request.POST["Nombre"], Apellido=request.POST["Apellido"],
                                     Email=request.POST["Email"], Celular=request.POST["Celular"], Fecha_Ingreso_Empresa=request.POST["Fecha_Ingreso_Empresa"])
        return redirect('/Operario/')

    def put(self, request, User):
        datos = json.loads(request.body)
        ope = list(Operario.objects.filter(UserID=User).values())
        if len(ope) > 0:
            NewUser = Operario.objects.get(UserID=User)
            NewUser.UserID = datos['UserID']
            NewUser.Nombre = datos['Nombre']
            NewUser.Apellido = datos['Apellido']
            NewUser.Email = datos['Email']
            NewUser.Celular = datos['Celular']
            NewUser.Fecha_Ingreso_Empresa = datos['Fecha de Ingreso Empresa']
            NewUser.save()
            mensaje = {"Respuesta": "Se actualizaron los datos correctamente"}
        else:
            mensaje = {"Respuesta": "No se encontraron datos"}
        return JsonResponse(mensaje)

    def delete(self, request, User):
        ope = list(Operario.objects.filter(UserID=User).values())
        if len(ope) > 0:
            Operario.objects.filter(UserID=User).delete
            mensaje = {"Respuesta": "El registro se elimino correctamente"}
        else:
            mensaje = {"Respuesta": "No se encontraron datos"}
        return JsonResponse(mensaje)


class LoginViews(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, User=0):
        if User > 0:
            adm = list(Login.objects.filter(Documento=User).values())
            if len(adm) > 0:
                respuesta = adm[0]
                datos = {"Login": respuesta}
            else:
                datos = {"Respuesta": "No se encontrarton datos"}
        else:
            adm = list(Login.objects.values())
            datos = {'listadoLogin': adm}
        return JsonResponse(datos)

    def post(self, request):
        user = json.loads(request.body)
        admon = Administrador.objects.get(UserID=user["UserID"])
        Login.objects.create(Documento=user["Documento"], UserName=user["UserName"],
                             Clave=user["Clave"], Rol=user["Rol"], UserID=admon)
        return JsonResponse(user)


def Autenticacion(request):
    if request.method == 'POST':
        try:
            Credencial_Usuario = Login.objects.get(
                UserName=request.POST['UserName'], Clave=request.POST['Clave'])

            if Credencial_Usuario.Rol == "Administrador":
                request.session['UserName'] = Credencial_Usuario.UserName
                return render(request, 'gestionAdmon.html')
            elif Credencial_Usuario.Rol == "Operario":
                request.session['UserName'] = Credencial_Usuario.UserName
                return render(request, 'gestionOperario.html')
        except Login.DoesNotExist as e:
            message.success(request, "No hay registros existentes")
    return render(request, 'loginUser.html')


def formularioRegistroAdmon(request):
    return render(request, "registroAdmon.html")


def fomularioctualizar(request, UserID):
    admon = Administrador.objects.get(UserID=UserID)
    datos = {
        'admon': admon
    }
    return render(request, "actualizarAdmon.html", datos)


def actualizar(request):
    user = request.POST['UserID']
    nom = request.POST['Nombre']
    ape = request.POST['Apellido']
    ema = request.POST['Email']
    cel = request.POST['Celular']
    fec = request.POST['Fecha_Ingreso_Empresa']
    admon = Administrador.objects.get(UserID=user)
    UserID = admon
    admon.UserID = user
    admon.Nombre = nom
    admon.Apellido = ape
    admon.Email = ema
    admon.Celular = cel
    admon.Fecha_Ingreso_Empresa = fec
    admon. save()
    return redirect('/Administrador/')


def eliminarAdmon(request, UserID):
    Administrador.objects.filter(UserID=UserID).delete()
    return redirect('/Administrador/')

def consultarjoin(request,UserID):
    datos = Perfil_Empresa.objects.select_related('UserID').filter(UserID = UserID)
    tamplate_name="consultarDatosAdmon.html"
    resultado={"lista":datos}
    return render(request,tamplate_name,resultado)

def consultarempresa(request,UserID):
    datos = Perfil_Empresa.objects.select_related('ID_Empresa').filter(ID_Empresa = UserID)
    tamplate_name="consultarEmpresa.html"
    resultado={"lista":datos}
    return render(request,tamplate_name,resultado)

def nuevatransccion(request):
    NumCuenta = request.POST['Numero_Cuenta']
    Datetrans = request.POST['Fecha_Transaccion']
    ValorTra = request.POST['Valor_Transaccion']
    admon = Perfil_Empresa.objects.get(ID_Empresa=ID_Empresa)
    ID_Empresa= ID_Empresa
    admon. save()
    return redirect('/consultarEmpresa/')

def deletetransccion(request,ID_Empresa):
        ope = list(Transacciones.objects.filter(ID_Empresa=ID_Empresa).values())
        Transacciones.objects.filter(ID_Empresa=ID_Empresa).delete
        return JsonResponse('/consultarDatosEmpresa/')


def formularioRegistroOpera(request):
    return render(request, "registroOpera.html")


def fomularioctualizarOpera(request, UserID):
    opera = Operario.objects.get(UserID=UserID)
    datos = {
        'opera': opera
    }
    return render(request, "actualizarOpera.html", datos)


def actualizarOpera(request):
    user = request.POST['UserID']
    nom = request.POST['Nombre']
    ape = request.POST['Apellido']
    ema = request.POST['Email']
    cel = request.POST['Celular']
    fec = request.POST['Fecha_Ingreso_Empresa']
    opera = Operario.objects.get(UserID=user)
    UserID = opera
    opera.UserID = user
    opera.Nombre = nom
    opera.Apellido = ape
    opera.Email = ema
    opera.Celular = cel
    opera.Fecha_Ingreso_Empresa = fec
    opera. save()
    return redirect('/Operario/')


def eliminarOpera(request, UserID):
    Operario.objects.filter(UserID=UserID).delete()
    return redirect('/Operario/')

def consultarjoinOpera(request,UserID):
    datos = Perfil_Empresa.objects.select_related('UserID').filter(UserID = UserID)
    tamplate_name="consultarDatosOpera.html"
    resultado={"lista":datos}
    return render(request,tamplate_name,resultado)
