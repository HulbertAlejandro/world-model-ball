# World Model Ball

Proyecto académico sobre **World Models**, enfocado en el aprendizaje de la dinámica de un entorno controlable de bola rebotante y el uso de sus predicciones para el control mediante imaginación.

## Estado actual

🟢 **Entorno implementado y dataset generado.**

Actualmente el proyecto cuenta con:

* Entorno 2D personalizado de bola rebotante.
* Simulación de gravedad y movimiento.
* Colisiones con paredes laterales.
* Plataforma controlable horizontalmente.
* Tres acciones: izquierda, quieto y derecha.
* Sistema de recompensas.
* Control del ciclo de vida de los episodios.
* Visualización interactiva mediante Pygame.
* Generación de datos mediante exploración aleatoria.
* Dataset de **53.630 transiciones** correspondientes a **1.000 episodios**.
* Análisis y validación del dataset.

La siguiente etapa es implementar y evaluar el **World Model predictivo**.

## Instalación

### 1. Crear el entorno virtual

```bash
python -m venv .venv
```

### 2. Activar el entorno virtual

En Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

## Ejecutar el entorno

Para ejecutar la visualización interactiva:

```bash
python -m environment.run_game
```

### Controles

* `←` mover la plataforma hacia la izquierda.
* `→` mover la plataforma hacia la derecha.
* `R` reiniciar el episodio.
* `ESC` salir.

## Generación del dataset

Para generar el dataset mediante exploración aleatoria:

```bash
python -m data.collect_data
```

El dataset se guarda en:

```text
data/ball_dataset.npz
```

El archivo contiene:

* `states`: estados actuales.
* `actions`: acciones ejecutadas.
* `next_states`: estados siguientes.
* `rewards`: recompensas.
* `dones`: indicador de finalización del episodio.

## Análisis del dataset

Para analizar y validar los datos:

```bash
python -m data.analyze_data
```

El análisis incluye:

* Número de experiencias.
* Distribución de acciones.
* Distribución de recompensas.
* Número de episodios terminados.
* Estadísticas de las variables del estado.
* Validación de valores `NaN`.
* Validación de acciones.

## Representación del estado

El estado actual del entorno se representa mediante el vector:

```text
[x, y, vx, vy, paddle_x]
```

Donde:

* `x`: posición horizontal de la bola.
* `y`: posición vertical de la bola.
* `vx`: velocidad horizontal.
* `vy`: velocidad vertical.
* `paddle_x`: posición horizontal de la plataforma.

## Acciones

El agente dispone de tres acciones:

```text
0 = izquierda
1 = quieto
2 = derecha
```

## Recompensas

```text
+1  → rebote exitoso en la plataforma
 0  → transición normal
-10 → bola perdida
```

## Estructura

```text
world-model-ball/
├── .venv/
├── environment/
│   ├── ball_env.py
│   └── run_game.py
├── data/
│   ├── collect_data.py
│   ├── analyze_data.py
│   └── ball_dataset.npz
├── .gitignore
├── README.md
└── requirements.txt
```

> `ball_dataset.npz` es un archivo generado localmente y está excluido del repositorio mediante `.gitignore`.

## Próximas etapas

1. Preparar los datos para entrenamiento y validación.
2. Implementar un baseline predictivo.
3. Implementar el World Model basado en una red neuronal recurrente LSTM.
4. Evaluar predicciones de uno y múltiples pasos.
5. Implementar control mediante imaginación.
6. Comparar el comportamiento del agente con y sin World Model.
7. Como extensión opcional, comparar LSTM con Transformer.
8. Como extensión adicional, explorar observaciones visuales.