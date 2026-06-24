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
    return 2 <= len(sigla) <= 5 and sigla.isalpha() and sigla.isupper()

def validar_nombre(nombre):
    return 3 <= len (nombre.strip()) <=40

def validar_fabricante(fabricante):
    return



def agregar_consola(consolas,ventas):
    sigla = input("Ingrese sigla : ")

    if not validar_sigla(sigla):
        print("Sigla invalida")
        return
    if sigla in consolas:
        print("La sigla ya existe")
        return
    


print("---MENU PRINCIPAL")
print("1.Agregar consola")
print("2.Buscar consola por sigla")
print("3.Eliminar consola")
print("4.Mostrar todas las consolas ")
print("5.Salir")