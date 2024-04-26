
class Contacto:
    def __init__ (self, nombre, telefono,edad):
        self.nombre=nombre
        self.telefono=telefono
        self.edad=edad

contactos=[]


while True:
    print("que deseas hacer?")
    print("1. ver lista de contactos")
    print("2. agregar un contacto")
    print("3. eliminar un contacto")
    print("4. buscar un contacto")
    print("0. salir")

    
    x=int(input("elige "))

    if x==1:
        for contacto in contactos:
            print(f"Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Edad: {contacto.edad}")
        
    elif x==2:
        a=input("escribe el nombre  ")
        b=input("escribe el numero ")
        c=input("escribe la edad ")
        nuevoContacto=Contacto(a,b,c)

        contactos.append(nuevoContacto)
        
        
    elif x==3:
        a=int(input("primer numero "))
        b=int(input("segundo numero "))

        print(a/b)
        
    elif x==4:
        a=int(input("primer numero "))
        b=int(input("segundo numero "))

        print(a*b)
        
    
    elif x==0:
        break
    else:
        print("no c puede")
        
