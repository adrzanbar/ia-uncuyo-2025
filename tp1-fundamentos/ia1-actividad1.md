# Actividad Preliminar 1

## 1. Ejemplos de aplicaciones de inteligencia artificial.

### AlphaFold

AlphaFold es un programa de inteligencia artificial desarrollado por DeepMind, filial de Alphabet, que realiza predicciones sobre la estructura de las proteínas. Está diseñado mediante técnicas de aprendizaje profundo.
AlphaFold 1 (2018) ocupó el primer lugar en la clasificación general de la 13ª Evaluación Crítica de Predicción de Estructuras (CASP) en diciembre de 2018. Fue particularmente exitoso en la predicción de las estructuras más precisas para los objetivos calificados como más difíciles por los organizadores de la competencia, donde no había estructuras de plantilla existentes disponibles de proteínas con secuencias parcialmente similares.
AlphaFold 2 (2020) repitió esta colocación en la competición CASP14 en noviembre de 2020. Alcanzó un nivel de precisión muy superior al de cualquier otro participante. Obtuvo una puntuación superior a 90 en la prueba de distancia global (GDT) de CASP para aproximadamente dos tercios de las proteínas, una prueba que mide la similitud entre una estructura predicha computacionalmente y la estructura determinada experimentalmente, donde 100 representa una coincidencia completa.
Los resultados de AlphaFold 2 en CASP14 fueron calificados de «asombrosos» y «transformadores». Sin embargo, algunos investigadores señalaron que la precisión era insuficiente para un tercio de sus predicciones, y que no revelaba el mecanismo subyacente ni las reglas del plegamiento de proteínas para el problema del plegamiento de proteínas, que sigue sin resolverse.
AlphaFold 3 se anunció el 8 de mayo de 2024. Puede predecir la estructura de complejos creados por proteínas con ADN, ARN, diversos ligandos e iones. El nuevo método de predicción muestra una mejora mínima del 50% en la precisión de las interacciones de proteínas con otras moléculas en comparación con los métodos existentes. Además, para determinadas categorías clave de interacciones, la precisión de la predicción se ha duplicado.

#### El Problema del Plegamiento de Proteínas
Las proteínas son las moléculas fundamentales de la vida: forman nuestros músculos, transportan oxígeno en la sangre, combaten infecciones y catalizan reacciones químicas esenciales. Sin embargo, para que una proteína pueda cumplir su función, debe adoptar una forma tridimensional específica, un proceso conocido como "plegamiento".

#### ¿Por qué es tan Difícil Predecir?
El número de formas posibles que puede adoptar una proteína es astronómico. Una proteína típica de 100 aminoácidos podría teóricamente plegarse en más configuraciones que átomos hay en el universo observable. Sin embargo, en la naturaleza, cada proteína encuentra su forma correcta en segundos o minutos. Esta paradoja se conoce como la "Paradoja de Levinthal".

#### ¿Por qué Queremos Resolver este Problema?

- Muchas enfermedades (Alzheimer, Parkinson, diabetes) están causadas por proteínas mal plegadas
- Conocer la estructura de una proteína permite diseñar medicamentos específicos que se ajusten perfectamente a ella, como una llave a su cerradura
- Diseñar nuevas enzimas para procesos industriales más eficientes y ecológicos
- Crear proteínas que puedan degradar plásticos o capturar CO₂

Antes de AlphaFold, determinar experimentalmente la estructura de una sola proteína podía tomar años de trabajo en laboratorio y costar millones de dólares. Por eso la predicción computacional de estructuras proteicas representa uno de los santos griales de la biología molecular.

Se sabe que DeepMind ha entrenado el programa con más de 170.000 proteínas del Protein Data Bank, un repositorio público de secuencias y estructuras de proteínas. El programa utiliza una forma de red de atención, una técnica de aprendizaje profundo que se centra en que la IA identifique las partes de un problema mayor y, a continuación, las junte para obtener la solución global. El entrenamiento global se llevó a cabo con una potencia de procesamiento de entre 100 y 200 GPU.

### OpenAI Five

OpenAI Five es un programa informático de OpenAI que juega al videojuego de cinco contra cinco Dota 2. Su primera aparición pública tuvo lugar en 2017, donde se demostró en una partida en vivo de uno contra uno contra el jugador profesional Dendi, que perdió contra él. Al año siguiente, el sistema había avanzado hasta el punto de funcionar como un equipo completo de cinco personas, y comenzó a jugar contra equipos profesionales y a demostrar su capacidad para derrotarlos.

Al elegir un juego tan complejo como Dota 2 para estudiar el aprendizaje automático, OpenAI pensó que podría capturar con mayor precisión la imprevisibilidad y la continuidad que se observan en el mundo real, construyendo así sistemas de resolución de problemas más generales. Los algoritmos y el código utilizados por OpenAI Five acabaron siendo tomados prestados por otra red neuronal en desarrollo por la empresa, una que controlaba una mano robótica física.

Cada bot de OpenAI Five es una red neuronal que contiene una sola capa con una LSTM de 4096 unidades que observa el estado actual del juego extraído de la API del desarrollador de Dota. La red neuronal realiza acciones a través de numerosas cabezas de acción posibles (no hay datos humanos implicados), y cada cabeza tiene un significado. Por ejemplo, el número de ticks para retrasar una acción, qué acción seleccionar, la coordenada X o Y de esta acción en una cuadrícula alrededor de la unidad. Además, las cabezas de acción se calculan de forma independiente. El sistema de IA observa el mundo como una lista de 20.000 números y realiza una acción llevando a cabo una lista de ocho valores de enumeración. Además, selecciona diferentes acciones y objetivos para entender cómo codificar cada acción y observar el mundo.

OpenAI Five se ha desarrollado como un sistema de entrenamiento de aprendizaje por refuerzo de propósito general sobre la infraestructura «Rapid». Rapid consta de dos capas: hace girar miles de máquinas y las ayuda a «hablar» entre sí y una segunda capa ejecuta software. En 2018, OpenAI Five había jugado alrededor de 180 años de aprendizaje por refuerzo ejecutándose en 256 GPU y 128 000 núcleos de CPU, utilizando Proximal Policy Optimization, un método de gradiente de políticas.
