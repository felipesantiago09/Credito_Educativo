class ErrorValorCompra(Exception):
    pass


class ErrorPlazo(Exception):
    """ Se usa cuando el numero de cuotas es menor que uno """
    pass


class ErrorUsura(Exception):
    """ Se usa cuando la tasa de interés sea superior a la maxima permitida por la ley """
    pass


class ErrorDatos(Exception):
    """ Se usa cuando los datos estén vacíos """
    pass


def calcular_cuota(compra, tasa, plazo):
    """
    Calcula la cuota a pagar por una compra de un credito educativo
    compra : Valor de la compra del credito
    tasa : Debe ser un porcentaje entre 0 y 0.04 (4%)
    plazo : numero de cuotas a diferir el credito
    """

   
    if compra is None or tasa is None or plazo is None:
        raise ErrorDatos("Los datos no pueden estar vacíos")

   
    if compra <= 0:
        raise ErrorValorCompra("El valor del credito educativo debe ser mayor que cero")

 
    if plazo <= 0 or plazo > 96:
        raise ErrorPlazo("El plazo no puede ser menor o igual a cero ni mayor a 96")

   
    if tasa > 4 / 100:
        raise ErrorUsura("La tasa es superior al máximo de usura de 4% mensual")

    
    if tasa == 0:
        return compra / plazo

    
    return (compra * tasa) / (1 - (1 + tasa) ** (-plazo))


def calcular_total_abonos(compra, tasa, plazo):
    cuota = calcular_cuota(compra, tasa, plazo)
    return cuota * plazo


def calcular_total_intereses(compra, tasa, plazo):
    total_abonos = calcular_total_abonos(compra, tasa, plazo)
    return total_abonos - compra