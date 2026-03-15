Simulador de Crédito Educativo
Integrantes

Juan Felipe Santiago

Jhairo Esteban Muñeton

----
Descripción del Proyecto

El Simulador de Crédito Educativo es un programa desarrollado en Python que permite calcular el comportamiento de un préstamo o crédito educativo a partir de tres datos principales:

Valor del crédito
Tasa de interés mensual
Plazo en meses
El sistema calcula automáticamente:
Cuota mensual
Total pagado al finalizar el crédito
Total de intereses generados

Además, el proyecto incluye:
Validación de datos de entrada
Manejo de errores mediante excepciones personalizadas
Pruebas unitarias para comprobar que los cálculos sean correctos

---------
Objetivo del Proyecto
El objetivo de este proyecto es simular el funcionamiento de un crédito educativo usando matemáticas financieras, permitiendo al usuario conocer:

cuánto pagará cada mes,
cuánto terminará pagando en total,
y cuánto dinero corresponde únicamente a intereses.

Esto ayuda a entender el costo real de financiar estudios mediante cuotas.

Funcionalidades del Sistema

--------
El programa permite:

Calcular la cuota fija mensual de un crédito educativo.
Calcular el total de abonos (suma de todas las cuotas).
Calcular el total de intereses generados durante todo el plazo.
Validar que los datos ingresados sean correctos.
Lanzar errores personalizados cuando los datos no cumplen las reglas.
Verificar el correcto funcionamiento con pruebas automáticas.

Datos de Entrada

El sistema recibe los siguientes datos:
1. Valor del crédito (compra)
Es el monto total solicitado para el crédito educativo.
Debe ser un número mayor que 0

Ejemplo:

20_000_000
15_000_000

2. Tasa de interés mensual (tasa)

Es el porcentaje de interés que se cobra cada mes.

Importante:

En el programa, la tasa se ingresa en formato decimal, no en porcentaje directo.

Ejemplos:

1.2% mensual → se escribe como 1.2 / 100 → 0.012
1.5% mensual → se escribe como 1.5 / 100 → 0.015
0.8% mensual → se escribe como 0.8 / 100 → 0.008

Límite permitido:

La tasa no puede ser mayor al 4% mensual

En decimal:

4 / 100 = 0.04

3. Plazo (plazo)

Es el número de meses en los que se pagará el crédito.

---------

Reglas:

Debe ser mayor que 0
No puede ser mayor a 96 meses

Datos de Salida

El sistema genera los siguientes resultados:

1. Cuota mensual

Valor fijo que el usuario debe pagar cada mes.

2. Total de abonos

Suma total de todas las cuotas pagadas durante el crédito.

3. Total de intereses

Diferencia entre el total pagado y el valor inicial del crédito.

Fórmulas Utilizadas

El proyecto utiliza la fórmula de cuota fija de un crédito amortizado.

1. Fórmula de la cuota mensual
Cuota
=
compra
×
tasa
1
−
(
1
+
tasa
)
−
plazo
Cuota=
1−(1+tasa)
−plazo
compra×tasa
	​


2. Total de abonos
Total de abonos
=
Cuota mensual
×
Plazo
Total de abonos=Cuota mensual×Plazo
3. Total de intereses
Total de intereses
=
Total de abonos
−
Valor del credito
Total de intereses=Total de abonos−Valor del credito

Caso Especial: Tasa 0%

Si la tasa de interés es 0%, el sistema no aplica la fórmula financiera, sino una división directa:

Cuota
=
compra
plazo
Cuota=
plazo
compra
	​


Esto significa que el crédito se paga sin intereses.

Validaciones del Sistema

El programa verifica que los datos cumplan ciertas condiciones antes de realizar los cálculos.

Se generan errores cuando:
1. El valor del crédito es menor o igual a cero

2. El plazo es menor o igual a cero

3. El plazo supera el máximo permitido

Máximo permitido: 96 meses

4. La tasa de interés supera el máximo permitido

Máximo permitido:

4% mensual

En decimal: 0.04

Ejemplo inválido:

5 / 100 = 0.05


5. Los datos están vacíos o incompletos


El sistema define excepciones propias para manejar errores de forma clara:

ErrorValorCompra
Se usa cuando el valor del crédito es menor o igual a cero.

ErrorPlazo
Se usa cuando el plazo es inválido (menor o igual a cero, o mayor a 96 meses).

ErrorUsura
Se usa cuando la tasa supera el máximo permitido del 4% mensual.

ErrorDatos
Se usa cuando faltan datos o están vacíos.


