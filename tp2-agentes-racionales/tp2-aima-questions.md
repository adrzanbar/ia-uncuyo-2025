# 5. Responder las preguntas 2.10 y 2.11 de AIMA 3ra Edición

## 2.10 Considera una versión modificada del entorno de aspiradora del ejercicio 2.8, en la que el agente recibe una penalización de un punto por cada movimiento.

> ### 2.8 Implemente un simulador de entorno que mida el rendimiento para el mundo de las aspiradoras que se muestra en la figura 2.2 y se especifica en la página 38.

![Figura 2.2](images/Figure%202.2.png)

> Consideremos el sencillo agente aspirador que limpia un cuadrado si está sucio y se desplaza al siguiente cuadrado si no lo está.
> Supongamos lo siguiente:
>
> - La medida de rendimiento otorga un punto por cada cuadrado limpio en cada paso temporal, a lo largo de una «vida útil» de 1000 pasos temporales.
> - La «geografía» del entorno se conoce a priori (Figura 2.2), pero no se conoce la distribución de la suciedad ni la ubicación inicial del agente. Los cuadrados limpios permanecen limpios y al aspirar se limpia el cuadrado actual. Las acciones Izquierda y Derecha mueven al agente hacia la izquierda y hacia la derecha, excepto cuando esto llevaría al agente fuera del entorno, en cuyo caso el agente permanece donde está.
> - Las únicas acciones disponibles son Izquierda, Derecha y Aspirar.
> - El agente percibe correctamente su ubicación y si esa ubicación contiene suciedad.

### a. ¿Puede un agente reflejo simple ser perfectamente racional en este entorno? Explica tu respuesta.

No. Dado que el agente, basándose únicamente en la percepción actual, no puede saber si ya exploró la otra celda, éste incurrirá en penalizaciones innecesarias oscilando entre las dos celdas.

### b. ¿Qué ocurre con un agente reflejo con estado? Diseña un agente de este tipo.

Un agente de éste tipo sí puede ser racional en este entorno, dado que en su estado puede mantener un registro de las celdas exploradas, evitando moverse una vez que haya explorado ambas.

### c. ¿Cómo cambian tus respuestas a las preguntas a y b si las percepciones del agente le proporcionan el estado limpio/sucio de cada cuadrado del entorno?

En este caso el agente reflejo simple (pregunta a) sí sería perfectamente racional, ya que puede dejar de moverse al detectar que todas las celdas están limpias.
El agente reflejo con estado (pregunta b) ya es racional, como se dijo, pero esta información extra le permite obtener una medida de desempeño aún mejor.
