# Buscaminas

## Descripción:
El juego consiste en despejar todas las casillas de un tablero que no ocultan una mina. Si un jugador revela una mina, pierde. Si se descubre una casilla con un número, este indica cuántas minas se ocultan en las 8 casillas circundantes. Si se descubre una casilla sin número (un espacio en blanco), significa que ninguna de las casillas vecinas tiene una mina, y estas se descubren automáticamente.

## Justificación de las habilidades cognitivas:
- **Memoria**: Recordar posiciones sospechosas de minas.
- **Reconocimiento de patrones**: Analizar la disposición de los números para inferir la posición de las minas.
- **Estimulación cerebral**: Se requiere esfuerzo mental significativo para resolver el juego.
- **Manejo del estrés**: El riesgo de descubrir una mina puede generar estrés, y gestionarlo es esencial para el éxito.

## Antecedentes:
Se investigaron los efectos de juegos como el Buscaminas en un asilo de ancianos, resultando en una mejora significativa de las habilidades cognitivas y el bienestar general de los residentes. En el libro “Focus” de Daniel Goleman, se documenta el caso de un estudiante que, tras dedicar considerable tiempo a este juego, pudo completar un tablero en solo un minuto y medio.

## Desafíos durante el diseño:
El principal desafío fue implementar la lógica para revelar múltiples casillas cuando se descubre una casilla sin minas circundantes. La solución involucró el uso de condicionales y un diseño de tablero predeterminado.

## Plan de pruebas:
| Entradas       | Fila | Columna | Resultado                                      |
|----------------|------|---------|------------------------------------------------|
| Casilla válida | 1    | 1       | Se despejan las casillas                       |
| Valores repetidos | 1    | 1       | Valores repetidos                          |
| Casilla con mina | 7    | 1       | Has perdido                                     |
| Fuera de rango  | -1   | 1       | Valores fuera de rango                         |

## Código:

Se presenta un fragmento del código principal:
```python
def main():
    # Creación de tableros: escondido, para ganar y vacío.
    tablero_escondido = ...
    tablero_ganar = ...
    tablero_vacio = ...

    # Lógica del juego...
```

Para ejecutar el juego completo, consulte los archivos del repositorio.

## Cómo jugar:
1. Inicie el juego.
2. Ingrese la fila y la columna de la casilla que desea despejar.
3. Continúe descubriendo casillas hasta ganar o encontrar una mina.

¡Buena suerte y disfrute del juego!

---

Por favor, consulte la documentación completa y otros archivos relacionados en este repositorio para más detalles y para obtener el juego completo.
