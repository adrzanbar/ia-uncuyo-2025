# Respuestas Trabajo Práctico 7A: Introducción a ML

## Ejercicio 1

> En cada uno de los siguientes ejercicios, indique si en general se espera que un método de aprendizaje de máquinas flexible se comporte mejor o peor que uno inflexible. Justifique su respuesta.

### a) El tamaño de la muestra $n$ es extremadamente grande, y el número de predictores $p$ es pequeño.

Se espera que se comporte **Mejor**. Al tener una gran cantidad de observaciones ($n$), el riesgo de sobreajuste disminuye y la varianza del modelo baja. Esto le permite aprovechar su flexibilidad para aprender relaciones complejas y reducir el sesgo sin pagar un costo alto en varianza. Además, como $p$ es pequeño, se evita que los datos queden dispersos en demasiadas dimensiones (maldición de la dimensionalidad), lo que favorece a los métodos locales y no paramétricos.

### b) El número de predictores $p$ es extremadamente grande, y el número de observaciones $n$ es pequeño.

Se espera que se comporte **Peor**. Con pocas observaciones y muchas variables, el espacio queda casi vacío (maldición de la dimensionalidad). Un método flexible tenderá a memorizar el ruido o patrones casuales de esa pequeña muestra, disparando la varianza del modelo (sobreajuste severo). En este caso es preferible un método inflexible porque su propia rigidez limita las soluciones posibles y evita que se ajuste a esas fluctuaciones engañosas.

### c) La relación entre los predictores y la variable dependiente es altamente no lineal.

Se espera que se comporte **Mejor**. Un modelo inflexible (como la regresión lineal) impone una estructura rígida que no puede doblarse para seguir curvaturas pronunciadas, lo que produce un **sesgo sistemático muy alto**. Un método flexible tiene la capacidad de adaptarse a la verdadera forma no lineal de los datos, reduciendo el sesgo y logrando un menor error en datos de prueba.

### d) La varianza de los términos de error, $\sigma^2 = \text{Var}(\epsilon)$, es extremadamente alta.

Se espera que se comporte **Peor**. Cuando el ruido aleatorio ($\sigma^2$) es muy alto, las fluctuaciones en los datos de entrenamiento se deben principalmente al azar y no a la relación real entre las variables. Un modelo flexible intentará ajustar y seguir cada pico de ese ruido, lo que dispara la varianza de sus predicciones (sobreajuste). En cambio, un modelo inflexible impone una forma rígida que promedia y filtra las fluctuaciones aleatorias, rindiendo mucho mejor frente a datos nuevos.

---

## Ejercicio 2

> Explique si cada escenario representa un problema de clasificación o de regresión, e indique si el interés principal es inferir o predecir. Especifique $n$ (cantidad de observaciones) y $p$ (cantidad de predictores) en cada caso.

### a) Se recopila un conjunto de datos sobre las 500 empresas más importantes de Estados Unidos. Para cada una de las empresas se registran las ganancias, el número de empleados, la industria y el salario del director ejecutivo. Se tiene interés en comprender qué factores afectan el salario de los directores ejecutivos.

- **Tipo de problema:** Regresión
- **Interés principal:** Inferencia
- **$n$ (observaciones):** 500
- **$p$ (predictores):** 3 (ganancias, número de empleados e industria)

### b) Se está considerando lanzar un nuevo producto y se desea saber si será un éxito o un fracaso. Se recolectan datos de 20 productos similares que fueron lanzados previamente. Para cada producto se ha registrado si fue un éxito o un fracaso, el precio cobrado por el producto, el presupuesto de marketing, el precio de la competencia, y otras diez variables.

- **Tipo de problema:** Clasificación
- **Interés principal:** Predicción
- **$n$ (observaciones):** 20
- **$p$ (predictores):** 13 (precio cobrado, presupuesto de marketing, precio de la competencia y las otras 10 variables)

### c) Se tiene interés en predecir el % de cambio en el tipo de cambio USD/Euro en relación a los cambios semanales en los mercados de valores mundiales. Para eso se recolectan datos semanalmente durante todo el 2021. Para cada semana se registran el % de cambio de USD/Euro, el % de cambio en el mercado estadounidense, el % de cambio en el mercado británico, y el % de cambio en el mercado alemán.

- **Tipo de problema:** Regresión
- **Interés principal:** Predicción
- **$n$ (observaciones):** 52 (las 52 semanas del año 2021)
- **$p$ (predictores):** 3 (% de cambio en EE. UU., % de cambio en Reino Unido y % de cambio en Alemania)

---

## Ejercicio 3

> ¿Cuáles son las ventajas y desventajas de un enfoque muy flexible (versus uno menos flexible) para la regresión o clasificación? ¿Bajo qué circunstancias podría preferirse un enfoque más flexible a uno menos flexible? ¿Cuándo podría preferirse un enfoque menos flexible?

### Ventajas y desventajas de un enfoque muy flexible

- **Ventajas:** Presenta un menor sesgo (*bias*) y tiene la capacidad de ajustarse a relaciones verdaderas altamente no lineales o complejas entre los predictores y la variable de respuesta.
- **Desventajas:** Presenta una varianza más alta y un riesgo elevado de sobreajuste (*overfitting*), ya que puede seguir el ruido o los errores aleatorios de los datos de entrenamiento; además, reduce drásticamente la interpretabilidad del modelo.

### ¿Bajo qué circunstancias podría preferirse un enfoque más flexible?

- **Objetivo de predicción:** Cuando la meta principal es maximizar la exactitud predictiva y no se requiere comprender la relación individual de cada predictor.
- **No linealidad severa:** Cuando la verdadera función subyacente $f$ es marcadamente no lineal.
- **Muestra grande ($n$ grande en relación con $p$):** Cuando se cuenta con una gran cantidad de observaciones para entrenar el modelo, lo cual mitiga la varianza.
- **Bajo nivel de ruido:** Cuando la varianza irreducible del error $\text{Var}(\epsilon)$ es pequeña.

### ¿Cuándo podría preferirse un enfoque menos flexible?

- **Objetivo de inferencia:** Cuando se busca entender con claridad cómo influye cada predictor en la respuesta y evaluar pruebas de hipótesis estadísticas.
- **Muestra reducida ($n$ pequeño o $p$ grande):** Cuando hay pocas observaciones o muchos predictores, evitando el sobreajuste gracias a su baja varianza.
- **Relación cercana a la linealidad:** Cuando la relación subyacente real entre las variables es aproximadamente lineal.
- **Alto nivel de ruido:** Cuando los datos contienen errores aleatorios elevados, evitando memorizar fluctuaciones espurias.

---

## Ejercicio 4

> Describa las diferencias entre un enfoque paramétrico y uno no paramétrico. ¿Cuáles son las ventajas y desventajas de un enfoque paramétrico para regresión o clasificación, a diferencia de un enfoque no paramétrico?

### a) Diferencias entre ambos enfoques

- **Enfoque paramétrico:** Asume una forma funcional explícita para la función $f$ (por ejemplo, una relación lineal), y luego utiliza los datos de entrenamiento para estimar un número fijo de parámetros.
- **Enfoque no paramétrico:** No hace ninguna suposición explícita *a priori* sobre la forma funcional de $f$; en su lugar, busca estimar la función aproximándose a las observaciones de entrenamiento sin restringirse a una ecuación predefinida.

### b) Ventajas del enfoque paramétrico (frente al no paramétrico)

- **Simplificación del problema:** Reduce la tarea de estimar una función arbitraria de dimensión $p$ a estimar únicamente un conjunto pequeño y fijo de coeficientes.
- **Menor requerimiento de datos:** Puede ajustarse de manera adecuada con muestras de tamaño $n$ significativamente menores que las requeridas por los métodos no paramétricos.
- **Alta interpretabilidad:** Facilita la interpretación y la inferencia directa de los efectos marginales de cada variable.

### c) Desventajas del enfoque paramétrico (frente al no paramétrico)

- **Riesgo de mala especificación del modelo:** Si la forma funcional supuesta difiere mucho de la verdadera $f$, el modelo tendrá un sesgo alto y un mal ajuste, sin importar cuántos datos se recolecten.
- **Falta de adaptabilidad a patrones complejos:** No se adapta de manera natural a fluctuaciones intrincadas o curvaturas locales que no hayan sido contempladas en la estructura impuesta.

---

## Ejercicio 5

> La siguiente tabla muestra un conjunto de entrenamiento que consta de seis observaciones, tres predictores, y una variable dependiente cualitativa. Suponga que se quiere usar este *dataset* para predecir $Y$ cuando $X_1 = X_2 = X_3 = 0$ usando $K$ vecinos más cercanos (KNN).

| Obs. | $X_1$ | $X_2$ | $X_3$ | $Y$ |
| :---: | :---: | :---: | :---: | :---: |
| 1 | 0 | 3 | 0 | Rojo |
| 2 | 2 | 0 | 0 | Rojo |
| 3 | 0 | 1 | 3 | Rojo |
| 4 | 0 | 1 | 2 | Verde |
| 5 | -1 | 0 | 1 | Verde |
| 6 | 1 | 1 | 1 | Rojo |

### a) Calcule la distancia Euclidiana entre cada observación y el punto de prueba $X_1 = X_2 = X_3 = 0$.

La distancia euclidiana al origen $(0,0,0)$ se calcula mediante $d = \sqrt{(X_1 - 0)^2 + (X_2 - 0)^2 + (X_3 - 0)^2}$:

- **Obs. 1:** $\sqrt{0^2 + 3^2 + 0^2} = \sqrt{9} = 3$
- **Obs. 2:** $\sqrt{2^2 + 0^2 + 0^2} = \sqrt{4} = 2$
- **Obs. 3:** $\sqrt{0^2 + 1^2 + 3^2} = \sqrt{10} \approx 3.16$
- **Obs. 4:** $\sqrt{0^2 + 1^2 + 2^2} = \sqrt{5} \approx 2.24$
- **Obs. 5:** $\sqrt{(-1)^2 + 0^2 + 1^2} = \sqrt{2} \approx 1.41$
- **Obs. 6:** $\sqrt{1^2 + 1^2 + 1^2} = \sqrt{3} \approx 1.73$

### b) ¿Cuál es la predicción con $K = 1$? Justifique.

La predicción es **Verde**. Con $K = 1$, el algoritmo clasifica según el único vecino más cercano al punto $(0,0,0)$. La menor distancia corresponde a la **Observación 5** ($d = \sqrt{2} \approx 1.41$), cuya clase es **Verde**.

### c) ¿Cuál es la predicción con $K = 3$? Justifique.

La predicción es **Rojo**. Los 3 vecinos más cercanos al origen son:
1. **Obs. 5** ($d \approx 1.41$) $\rightarrow$ **Verde**
2. **Obs. 6** ($d \approx 1.73$) $\rightarrow$ **Rojo**
3. **Obs. 2** ($d = 2$) $\rightarrow$ **Rojo**

Por votación mayoritaria entre los 3 vecinos más cercanos (2 **Rojo** frente a 1 **Verde**), la clase predicha es **Rojo**.

### d) Si el límite de decisión de Bayes en este problema es altamente no lineal, ¿se espera que el mejor valor para $K$ sea grande o pequeño? ¿Por qué?

Se espera que el mejor valor para $K$ sea **pequeño**. Un valor pequeño de $K$ produce un modelo más flexible con límites de decisión irregulares y locales, capaces de adaptarse a fronteras altamente no lineales (bajo sesgo). Por el contrario, un valor grande de $K$ promedia muchos vecinos de regiones amplias, suavizando en exceso la frontera hasta volverla casi lineal y aumentando considerablemente el sesgo.