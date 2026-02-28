# Simulador de Crédito Educativo

## Integrantes
- Juan Felipe Santiago  
- Jhairo Esteban Muñeton  

---

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de un simulador de crédito educativo en Python.

El sistema permite calcular:

- La cuota mensual.
- El total pagado al finalizar el crédito.
- El total de intereses generados.

El programa valida los datos ingresados y maneja errores mediante excepciones personalizadas.  
También incluye pruebas unitarias para verificar que los cálculos sean correctos.

---

## Datos de Entrada

El programa recibe:

- **Valor de la compra:** monto total del crédito.
- **Tasa de interés mensual:** porcentaje mensual (ejemplo: 1.2%).
- **Plazo:** número de meses en los que se pagará el crédito.

---

## Datos de Salida

El sistema genera:

- **Cuota mensual**
- **Total de abonos**
- **Total de intereses**

---

## Validaciones

El sistema genera errores cuando:

- El valor del crédito es negativo.
- La tasa supera el máximo permitido.
- El plazo es mayor al permitido.
- El plazo es negativo o cero.
- Los datos están incompletos.
