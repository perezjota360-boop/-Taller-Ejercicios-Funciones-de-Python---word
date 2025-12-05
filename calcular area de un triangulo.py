#zona de codigo principal
def capturar_datos():
    numero_base = int(input("Ingrese un numero base: "))
    return numero_base

def capturar_altura():
    numero_altura = int(input("Ingrese un numero altura: "))
    return numero_altura
def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area 

def mostrar_resultado(area):
    print ("el area del trianguolos es:" + str(area))
    
  
#programa principal
base = capturar_datos()
altura = capturar_altura()
area = calcular_area_triangulo(base, altura)
mostrar_resultado(area)

