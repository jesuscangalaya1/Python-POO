#Zona de Clases
class Persona():
    def __init__(self,nom="",dir=""):
        self.nombre=nom
        self.direccion=dir
        self.__activo=False
    def getactivo(self):
        return  self.__activo
    def activa(self):
        self.__activo=True
    def __str__(self):
        return self.nombre+" "+self.direccion

class Docente(Persona):
    def __init__(self,objalumno:object,nom="",dir="",sue=0,tel=""):
        super().__init__(nom,dir)
        self.sueldo=sue
        self.telefono=tel
        self.objalumno=objalumno
    def califica(self):
        if(self.objalumno.vez==1):
            pr=(self.objalumno.nota1+self.objalumno.nota2)/2
        else:
            pr=(self.objalumno.nota1+2*self.objalumno.nota2)/3
        self.objalumno.promedio=pr
    def __str__(self):
        return self.nombre+" Teléfono:"+self.telefono

class Alumno():
    def __init__(self,nom="",n1=None,n2=None,vz=1):
        self.nombre=nom
        self.nota1=n1
        self.nota2=n2
        self.vez=vz
        self.promedio=None
        self.__pago=350
    def getpago(self):
        return self.__pago
    def __generapago(self):
        if(self.promedio>=16):
            return 100
        elif(self.promedio>=14):
            return 300
        else:
            return 500
    def actpago(self):
        if(self.vez==3):
            self.__pago=self.__pago+self.__generapago()
        else:
            if(self.vez==2):
                self.__pago=self.__pago+0.5*self.__generapago()
    def __str__(self):
        if(self.promedio==None):
            return(self.nombre+" "+str(self.nota1)+" "
            +str(self.nota2)+" Nro de vez:"+str(self.vez))
        else:
            return(self.nombre+" "+str(self.nota1)+" "+str(self.nota2)+" "
            +" Nro de vez:"+str(self.vez)+" PR:"+str(self.promedio))

#PRG main
import os
os.system("cls")
objalu1=Alumno()
for i in range(2):
    while(True):
        nom=input("Ingrese el nombre del alumno:").strip()
        if(nom!=""):
            break
        else:
            print("Error")
    objalu1.nombre=nom
    while(True):
        n1=input("Ingrese la nota 1:").strip()
        if(n1!=""):
            if(n1.isdigit()):
                if(float(n1)>=0)and(float(n1)<=20):
                    break
                else:
                    print("Error")
            else:
                print("Error")
        else:
            print("Error")
    objalu1.nota1=float(n1)
    while(True):
        n2=input("Ingrese la nota 2:").strip()
        if(n2!=""):
            if(n2.isdigit()):
                if(float(n2)>=0)and(float(n2)<=20):
                    break
                else:
                    print("Error")
            else:
                print("Error")
        else:
            print("Error")
    objalu1.nota2=float(n2)
    while(True):
        nro=input("Ingrese El nro vez que lleva el curso:").strip()
        if(nro!=""):
            if(nro.isdigit()):
                if(int(nro)>1)and(int(nro)<=3):
                    break
                else:
                    print("Error")
            else:
                print("Error")
        else:
            print("Error")
    objalu1.vez=int(nro)
    print("Datos del alumno:")
    print(objalu1)
    print("Datos del docente que va generar Calificaciones:")
    while(True):
        nom=input("Ingrese el nombre del docente:").strip()
        if(nom!=""):
            break
        else:
            print("Error")
    while(True):
        dire=input("Ingrese la dirección del docente:").strip()
        if(dire!=""):
            break
        else:
            print("Error")
    while(True):
        sue=input("Ingrese el sueldo:").strip()
        if(sue!=""):
            if(sue.isdigit()):
                if(float(sue)>=1100):
                    break
                else:
                    print("Error")
            else:
                print("Error")
        else:
            print("Error")
    while(True):
        tel=input("Ingrese el teléfono:").strip()
        if(tel!=""):
            if(tel.isdigit()):
                if(len(tel)==9):
                    break
                else:
                    print("Error")
            else:
                print("Error")
        else:
            print("Error")
    objdoc1=Docente(objalu1,nom,dire,float(sue),tel)
    print(objdoc1)
    print("El docente tiene memoradums si/no? :")
    while(True):
        op=input().upper()
        if(op=="SI")or(op=="NO"):
            break
        else:
            print("Error")
    if(op=="NO"):
        objdoc1.activa()
        if (objdoc1.getactivo()):
            print("Generando Calificaciones...!!!")
            objdoc1.califica()
            print("Promedio obtenido por el alumno:")
            print(objalu1)
            print("Actualizando pago, ya que el Pago es en base al PROMEDIO:")
            objalu1.actpago()
            print("El pago será de:",objalu1.getpago())
        else:
            print("NO Puede registrar calificaciones pork no esta activo...!!!")
    else:
        print("NO Puede registrar calificaciones pork tiene MEMOS...!!!")

