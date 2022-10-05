from django.urls import path
from .views import AdministradorViews, LoginViews
from . import views


urlpatterns=[

    path('Administrador/',AdministradorViews.as_view(), name="Listar"),
    path('administrador/<int:User>',AdministradorViews.as_view(), name="Actualizar"),
    path('login/',LoginViews.as_view(), name="Credenciales"),
    path('loginUser/',views.Autenticacion, name="login Usuario"),
    path('formularioRegistroAdmon/', views.formularioRegistroAdmon,name="Registro de Admon"),
    path('actualizarAdmon/<int:UserID>',views.fomularioctualizar,name="Actualizar formulario"),
    path('actualizarAdmon/',views.actualizar, name="actualizar"),
    path('eliminarAdmon/<int:UserID>',views.eliminarAdmon, name="eliminarAdmon"),
    path('consultarDatosAdmon/<int:UserID>',views.consultarjoin, name="Consultar Datos Admon"),
    path('consultarDatosEmpresa/<int:UserID>',views.consultarempresa, name="Consultarempresa"),
    path('ingresartransccion',views.nuevatransccion, name="nuevatransccion"),
    path('borrartransccion/',views.deletetransccion, name="borrartransccion"),
    path('Operario/',OperarioViews.as_view(), name="Listar"),
    path('operario/<int:User>',OperarioViews.as_view(), name="Actualizar"),
    path('formularioRegistroOpera/', views.formularioRegistroOpera,name="Registro de Opera"),
    path('actualizarOpera/<int:UserID>',views.fomularioctualizarOpera,name="Actualizar formulario"),
    path('actualizarOpera/',views.actualizarOpera, name="actualizar"),
    path('eliminarOpera/<int:UserID>',views.eliminarOpera, name="eliminarOpera"),
    path('consultarDatosOpera/<int:UserID>',views.consultarjoinOpera, name="Consultar Datos Opera"),
]
