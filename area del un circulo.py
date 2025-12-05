#zona de funciones

def capturar_radio():
    radio= float(input("dijite el radio: "))
    return radio
def calcular_area(radio):
    area= (3.1416 * radio **2)
    return area
def mostrar_mensaje(area):
 mensaje= ("el area del cierculo es:" + str (area))
 return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)
    return mensaje
# zona de codigo principal

dato_radio =capturar_radio()
dato_area = calcular_area(dato_radio)
mensaje = mostrar_mensaje(dato_area)
mostrar_mensaje(mensaje)
