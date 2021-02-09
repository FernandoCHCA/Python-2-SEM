# Programa de José Fernando Chavez Castillo 
# 1972147

#INSTRUCCIONES
#Suponiendo que un coche viaja únicamente a 80 km por hora 
#¿Qué distancia recorre con $500 pesos, y en cuánto tiempo lo hace? [En horas y minutos]

# AQUI DEFINO UN SEPARADOR PARA SEPARAR CADA APARTADO PARA QUE SE PUEDA DIFERENCIAR MEJOR
def Separador(caracter,cantidad):
     SeparadorF = ""
     for numVeces in range(cantidad):
         SeparadorF=SeparadorF + caracter
     return SeparadorF
print(Separador("*",20))

# Variables previamente declaradas 

velocidad_km = float(80)
dinero_actual = float(500)

# Declaración de variables

print(Separador("*",20))

#AQUI PRIMERO PEDIMOS EL RENDIMIENTO 
print("Ingrese el rendimiento:")
rendimiento = float(input())

#AQUI EN CASO DE QUE LA RESPUESTA SEA MENOR A CERO SE LE DIRA QUE NO ES VALIDO Y QUE VUELVA A RESPONDER
while rendimiento<0:
    print("Error -> Deberia ser un numero positivo")
    rendimiento = float(input("Ingrese el rendimiento:"))

print(Separador("*",20))

#AQUI PRIMERO PEDIMOS EL PRECIO DE LA GASOLINA POR LITRO
print("Ingrese el precio de la gasolina [Por litro]:")
precio_gasolina = float(input())

#AQUI EN CASO DE QUE LA RESPUESTA SEA MENOR A CERO SE LE DIRA QUE NO ES VALIDO Y QUE VUELVA A RESPONDER
while precio_gasolina<0:
    print("Error -> Deberia ser un numero positivo")
    precio_gasolina = float(input("Ingrese el precio de la gasolina [Por litro]:"))

# Operaciones lógicas del programa

gasolina = (dinero_actual / precio_gasolina)
distancia_final = gasolina * rendimiento
tiempo_formato_decimal = distancia_final / velocidad_km
tiempo_formato_hora = int(tiempo_formato_decimal)
tiempo_formato_minutos = int((60)*(tiempo_formato_decimal-tiempo_formato_hora))

#AQUI POR ULTIMO PONEMOS EL RESULTADO
print(Separador("*",20))
print("Con $",dinero_actual,"pesos")
print("Se recorren",distancia_final,"km")
print("En",tiempo_formato_hora,"horas con",tiempo_formato_minutos,"minutos")