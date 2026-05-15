import sys 
sys.path.append('src')

from model import logica_Credito

try:
    print("Este programa le permite calcular la cuota a pagar por un credito educativo")

    monto = float(input("Monto del credito educativo: "))
    tasa = float(input("Tasa de interés del credito (%): "))
    plazo = int(input("Numero de cuotas en que va a diferir el credito: "))

    cuota = round(logica_Credito.calcular_cuota(monto, tasa, plazo), 2)

    print(f"La cuota mensual a pagar es de: {cuota}")

except Exception as err:
    print("No se pudo calcular la cuota")
    print(str(err))