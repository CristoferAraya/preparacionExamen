consolas ={
    "PS5": ["PlayStation 5", "Sony", 2020],
    "XSX": ["Xbox Series X", "Microsoft", 2020],
    "NSW": ["Nintendo Switch", "Nintendo", 2017]
}
ventas = {
    "PS5": [649990.0, 15],
    "XSX": [599990.0, 8],
    "NSW": [299990.0, 30]
}

def validar_sigla(sigla):
   if len(sigla) >= 2 and len(sigla) <=5:
       if sigla.isalpha():
           if sigla.isupper():
               return True
   return False

def validar_nombre(nombre):
   nombre = nombre.strip()
   if len(nombre) >= 3 and len(nombre) <= 40:
       return True
   else:
       return False

def validar_fabricante(fabricante):
    fabricante = fabricante.strip()
    if len(fabricante) >= 2 and len(fabricante) <= 30 :
        return True
    else:
        return False

def validar_año(anio):
    if anio >= 1972 and 2025:
        return True
    else:
        return False
    
def valida_precio(precio):
    if precio > 0:
        return True
    else:
        return False
    
def validar_stock(stock):
    if stock >= 0:
        return True
    else:
        return False


def mostrar_menu():
  print("\n==================")
  print("SISTEMA DE GESTION DE CONSOLAS")
  print("====================")
  print("1.Agregar consola")
  print("2.Buscar consola por sigla")
  print("3.Eliminar consola")
  print("4.Mostrar todas las consolas ")
  print("5.Salir")
  
def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opcion: "))
            
            if opcion >= 1 and opcion <= 5:
                return opcion
            else:
                print("Debe ingresar una opcion entre 1 y 5.")
        except ValueError:
            print("Debe ingresar un numero")