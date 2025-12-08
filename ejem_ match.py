# zona de funciones
def tomar_datos():
    print("dijite la letra A para actualizar sistema")
    print("dijite la letra E para borrar catalogo")
    print("dijite la letra S para salir del programa")
    print("dijite la letra c para crear producto")
    opcion = input("Seleccione una opción (A, E, S, C): ")
    return opcion
#hacer menu
def procesar_opcion(letra):
  while True: 
    letra = input().strip()
    if letra.lower() == "s":
        print("finalizo con exito")
        break
    else:
        print("sigue dentro del programa")
    return letra    
def gerar_mensaje(opcion, letra):
    mensaje = f"La {opcion} seleccionada es: {letra}"
    return mensaje
def imprimir_mensaje(mensaje):
   
    print(mensaje)
# zona principal
dato_opcion = tomar_datos()
dato_letra = procesar_opcion(dato_opcion)
dato_mensaje = gerar_mensaje(dato_opcion,dato_letra)
imprimir_mensaje(dato_mensaje)
