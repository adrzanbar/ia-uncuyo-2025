# 5. Responder las preguntas 2.10 y 2.11 de AIMA 3ra Edición

## 2.10 Considera una versión modificada del entorno de aspiradora del ejercicio 2.8, en la que el agente recibe una penalización de un punto por cada movimiento.

> ### 2.8 Implemente un simulador de entorno para medir el rendimiento del mundo de las aspiradoras que se muestra en la figura 2.2 y se especifica en la página 38. Su implementación debe ser modular, de modo que los sensores, los actuadores y las características del entorno (tamaño, forma, ubicación de la suciedad, etc.) se puedan cambiar fácilmente.

![Figura 2.2](images/Figure%202.2.png)

> Consideremos el sencillo agente aspirador que limpia un cuadrado si está sucio y se desplaza al siguiente cuadrado si no lo está.
> Supongamos lo siguiente:
>
> - La medida de rendimiento otorga un punto por cada cuadrado limpio en cada paso temporal, a lo largo de una «vida útil» de 1000 pasos temporales.
> - La «geografía» del entorno se conoce a priori (Figura 2.2), pero no se conoce la distribución de la suciedad ni la ubicación inicial del agente. Los cuadrados limpios permanecen limpios y al aspirar se limpia el cuadrado actual. Las acciones Izquierda y Derecha mueven al agente hacia la izquierda y hacia la derecha, excepto cuando esto llevaría al agente fuera del entorno, en cuyo caso el agente permanece donde está.
> - Las únicas acciones disponibles son Izquierda, Derecha y Aspirar.
> - El agente percibe correctamente su ubicación y si esa ubicación contiene suciedad.

> La implementación de este agente se encuentra en `student_agents/aima_simple_reflex_agent.py`

### a. ¿Puede un agente reflejo simple ser perfectamente racional en este entorno? Explica tu respuesta.

No. Dado que el agente, basándose únicamente en la percepción actual, no puede saber si ya exploró todas las celdas, una vez que todas las celdas estén limpias, este incurrirá en penalizaciones hasta agotar su vida útil.

### b. ¿Qué ocurre con un agente reflejo con estado? Diseña un agente de este tipo.

Un agente de éste tipo sí puede ser racional en este entorno, dado que en su estado puede mantener un registro de las celdas exploradas, evitando moverse una vez que haya explorado todas.
La implementación de este agente se encuentra en `student_agents/aima_simple_reflex_agent_with_state.py`

### c. ¿Cómo cambian tus respuestas a las preguntas a y b si las percepciones del agente le proporcionan el estado limpio/sucio de cada cuadrado del entorno?

En este caso el agente reflejo simple (pregunta a) sí sería perfectamente racional, ya que puede dejar de moverse al detectar que todas las celdas están limpias.
El agente reflejo con estado (pregunta b) ya es racional, como se dijo, pero esta información extra le permite obtener una medida de desempeño aún mejor.

## 2.11 Considera una versión modificada del entorno de vacío del ejercicio 2.8, en la que se desconoce la geografía del entorno (su extensión, límites y obstáculos), al igual que la configuración inicial de la suciedad. (El agente puede moverse hacia arriba y hacia abajo, así como hacia la izquierda y hacia la derecha).

> La imlpementación coincide con el ejercicio 2 del trabajo práctico, se puede encontrar en `student_agents/simple_reflex_agent.py`

### a. ¿Puede un agente reflejo simple ser perfectamente racional para este entorno? Explica tu respuesta.

Un agente reflejo no puede ser perfectamente racional. En entornos relativamente grandes en donde tenga que utilizar eficientemente los 1000 movimientos, al carecer de memoria, desperdiciará varios movimientos visitando celdas ya exploradas anteriormente.

### b. ¿Puede un agente reflejo simple con una función de agente aleatoria superar a un agente reflejo simple? Diseña un agente de este tipo y mide su rendimiento en varios entornos.

No. Tendría las mismas falencias que el agente anterior, y además podría no aspirar suciedad o aspirar donde no hay suciedad.

### c. ¿Puedes diseñar un entorno en el que tu agente aleatorio tenga un rendimiento deficiente? Muestra tus resultados.

En un entorno muy grande con un "pasillo" o "corredor" del que sólo existe una salida hacia donde se encuentra la suciedad. La probabilidad de que el agente aleatorio llegue a la posición de salida es baja, y aún cuando llegue se espera que efectivamente salga 1/4 de las veces que llega.

### d. ¿Puede un agente reflejo con estado superar a un agente reflejo simple? Diseña un agente de este tipo y mide su rendimiento en varios entornos. ¿Puedes diseñar un agente racional de este tipo?

Sí. El agente puede ir construyendo un modelo del entorno desconocido con cada percepción, permitiendole salir de entornos difíciles y utilizar eficientemente la cantidad limitada de movimientos, al no visitar nuevamente celdas ya exploradas.

> El entorno `harpomaxx/vacuum-cleaner-world` no soporta obstáculos ni grillas no cuadradas, una implementación de un agente reflejo simple con estado se encuentra en `student_agents/aima_simple_reflex_agent_with_sate.py`
