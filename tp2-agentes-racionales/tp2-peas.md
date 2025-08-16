# Para cada una de las siguientes actividades, describa el PEAS para cada tarea y caracterizarlo en término de las propiedades vistas

## a) Jugar al CS (o cualquier otro 3D Shooter)

### PEAS

| Medida de desempeño (P)                                        | Entorno (E)                                                               | Actuadores (A)                                     | Sensores (S)                                 |
| -------------------------------------------------------------- | ------------------------------------------------------------------------- | -------------------------------------------------- | -------------------------------------------- |
| - Tasa de victorias<br> - KDA (asesinatos/muertes/asistencias) | - Mapa del juego <br> - Oponentes <br> - Compañeros <br> - Objetivos <br> | - Teclado <br> - Mouse <br> - Micrófono <br> - API | - Pantalla <br> - Salida de audio <br> - API |

### Propiedades:

- Parcialmente observable
- Agente múltiple (competitivo y cooperativo)
- Determinista
- Secuencial
- Dinámico
- Continuo
- Conocido/Desconocido (depende del agente)

## b) Explorar los océanos

| Medida de desempeño (P)                           | Entorno (E)                                                                                                                                                                 | Actuadores (A)                           | Sensores (S)                                                                                  |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | --------------------------------------------------------------------------------------------- |
| - Área cubierta<br> - Calidad de las muestras<br> | - Terreno submarino<br> - Plantas<br> - Animales<br> - Obstáculos (rocas, naufragios, otros exploradores)<br> - Condiciones del agua (corrientes, temperatura, profundidad) | - Propulsores<br> - Brazos robóticos<br> | - Sensores de presión y temperatura<br> - Sonar / radar submarino<br> - Cámaras<br> - GPS<br> |

### Propiedades:

- Parcialmente observable
- Agente múltiple (competitivo)
- Estocástico
- Secuencial
- Dinámico
- Continuo
- Desconocido

## c) Comprar y vender tokens crypto (alguno)

| Medida de desempeño (P) | Entorno (E)                            | Actuadores (A)                                                 | Sensores (S)                            |
| ----------------------- | -------------------------------------- | -------------------------------------------------------------- | --------------------------------------- |
| - Ganancia neta         | - Mercado de criptomonedas (exchanges) | - Teclado y mouse<br> - API del exchange <br> - API de wallets | - Pantalla<br> - Cliente web <br> - API |

### Propiedades:

- Totalmente observable
- Agente múltiple (competitivo)
- Estocástico
- Secuencial
- Dinámico
- Continuo
- Conocido/Desconocido (depende del agente)

## d) Practicar tenis contra una pared

| Medida de desempeño (P)                                                                 | Entorno (E)                                            | Actuadores (A)                                      | Sensores (S)                                                                                                                                   |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------ | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| - Precisión de los golpes<br> - Número de golpes consecutivos<br> - Velocidad del golpe | - Pared<br> - Suelo<br> - Pelota de tenis<br> - Viento | - Brazo y mano<br> - Piernas o ruedas <br> - Tronco | - Visión 3D (cámaras, ojos)<br> - Propiocepción (giroscopio, acelerómetro, oído interno, sensores musculares)<br> - Audición (micrófono, oído) |

### Propiedades:

- Totalmente observable
- Agente simple
- Determinista
- Secuencial
- Estático
- Continuo
- Conocido

## e) Realizar un salto de altura

| Medida de desempeño (P)                                                                           | Entorno (E)                                                                                                        | Actuadores (A)                        | Sensores (S)                                                                                                   |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| - Altura lograda<br> - Eficiencia del salto (energía consumida)<br> - Seguridad (evitar lesiones) | - Pista de salto<br> - Barra horizontal<br> - Colchón de caída<br> - Condiciones ambientales (viento, temperatura) | - Piernas <br> - Brazos <br> - Tronco | - Propiocepción (giroscopio, acelerómetro, oído interno, sensores musuculares)<br> - Visión 3D (cámaras, ojos) |

### Propiedades:

- Totalmente observable
- Agente simple
- Determinista
- Secuencial
- Estático
- Continuo
- Conocido

## f ) Pujar por un artículo en una subasta.

| Medida de desempeño (P)                           | Entorno (E)                                                                                                | Actuadores (A)                                                          | Sensores (S)                                                                                                                     |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| - Precio de compra<br>- Eficiencia de presupuesto | - Sala o sistema de subasta<br>- Otros pujadores<br>- Reglas de la subasta<br>- Tiempo restante para pujar | - Dispositivo o medio para emitir pujas (palanca, botón, terminal, API) | - Ojos / cámara (humano) o API de lectura de estado (software) <br> - Oídos / micrófono (humano) o señales de eventos (software) |

### Propiedades:

- Parcialmente observable
- Agente múltiple (competitivo)
- Determinista
- Secuencial
- Estático
- Continuo
- Conocido
