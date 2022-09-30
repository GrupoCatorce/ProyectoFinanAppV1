from django.contrib import admin

from appFinanApp.models import Administrador,Operario,Perfil_Empresa,Transacciones

admin.site.register(Administrador)
admin.site.register(Operario)
admin.site.register(Perfil_Empresa)
admin.site.register(Transacciones)