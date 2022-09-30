from xml.dom.minidom import Document
from django.db import models

class Administrador(models.Model):
    UserID=models.IntegerField(primary_key=True)
    Nombre=models.CharField(max_length=30)
    Apellido=models.CharField(max_length=30)
    Email=models.EmailField()
    Celular=models.CharField(max_length=11)
    Fecha_Ingreso_Empresa=models.DateField()
    def __str__(self):
        return '%s %s %s %s %s %s'%(self.UserID,self.Nombre,self.Apellido,self.Email,self.Celular,self.Fecha_Ingreso_Empresa)

class Operario(models.Model):
    UserID=models.IntegerField(primary_key=True)
    Nombre=models.CharField(max_length=30)
    Apellido=models.CharField(max_length=30)
    Email=models.EmailField()
    Celular=models.CharField(max_length=11)
    Fecha_Ingreso_Empresa=models.DateField()
    def __str__(self):
        return '%s %s %s %s %s %s'%(self.UserID,self.Nombre,self.Apellido,self.Email,self.Celular,self.Fecha_Ingreso_Empresa)

class Perfil_Empresa(models.Model):
    ID_Empresa=models.IntegerField(primary_key=True)
    NIT=models.CharField(max_length=10)
    Nombre_Empresa=models.CharField(max_length=30)
    Email_Coorporativo=models.EmailField()
    Telefono_Coorporativo=models.CharField(max_length=11)
    UserID=models.ForeignKey(Administrador,on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s %s %s %s %s'%(self.ID_Empresa,self.NIT,self.Nombre_Empresa,self.Email_Coorporativo,self.Telefono_Coorporativo)

class Transacciones(models.Model):
    Numero_Cuenta=models.CharField(max_length=20,primary_key=True)
    Fecha_Transaccion=models.DateField()
    Valor_Transaccion=models.IntegerField()
    ID_Empresa=models.ForeignKey(Perfil_Empresa,on_delete=models.CASCADE)
    def __str__ (self):
        return '%s %s %s %s'%(self.Numero_Cuenta,self.Fecha_Transaccion,self.Valor_Transaccion)

class Login(models.Model):
    Documento=models.IntegerField(primary_key=True)
    UserName=models.CharField(max_length=30)
    Clave=models.CharField(max_length=30)
    Rol=models.CharField(max_length=30)
    UserID=models.ForeignKey(Administrador,on_delete=models.CASCADE)