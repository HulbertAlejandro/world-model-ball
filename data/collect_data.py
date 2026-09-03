import os

import numpy as np

from environment.ball_env import BallEnv


# -----------------------------
# Configuración
# -----------------------------

NUM_EPISODES = 1000
MAX_STEPS_PER_EPISODE = 500

OUTPUT_FILE = "data/ball_dataset.npz"


# -----------------------------
# Inicializar entorno y RNG
# -----------------------------

env = BallEnv()

rng = np.random.default_rng(42)


# -----------------------------
# Listas donde guardaremos
# las experiencias
# -----------------------------

states = []
actions = []
next_states = []
rewards = []
dones = []


# -----------------------------
# Generar episodios
# -----------------------------

for episode in range(NUM_EPISODES):

    # Cada episodio comienza con un
    # estado inicial aleatorio
    state = env.reset(
        randomize=True,
        rng=rng
    )

    episode_reward = 0.0

    for step in range(MAX_STEPS_PER_EPISODE):

        # Elegir una acción aleatoria
        action = rng.integers(0, 3)

        # Ejecutar acción
        next_state, reward, done = env.step(action)

        # Guardar experiencia
        states.append(state)
        actions.append(action)
        next_states.append(next_state)
        rewards.append(reward)
        dones.append(done)

        # Preparar siguiente estado
        state = next_state

        episode_reward += reward

        # Terminar episodio si la bola se pierde
        if done:
            break

    print(
        f"Episodio {episode + 1}/{NUM_EPISODES} | "
        f"Pasos: {env.step_count} | "
        f"Reward: {episode_reward:.1f}"
    )


# -----------------------------
# Convertir a NumPy
# -----------------------------

states = np.array(
    states,
    dtype=np.float32
)

actions = np.array(
    actions,
    dtype=np.int64
)

next_states = np.array(
    next_states,
    dtype=np.float32
)

rewards = np.array(
    rewards,
    dtype=np.float32
)

dones = np.array(
    dones,
    dtype=np.bool_
)


# -----------------------------
# Crear carpeta si no existe
# -----------------------------

os.makedirs(
    os.path.dirname(OUTPUT_FILE),
    exist_ok=True
)


# -----------------------------
# Guardar dataset
# -----------------------------

np.savez_compressed(
    OUTPUT_FILE,
    states=states,
    actions=actions,
    next_states=next_states,
    rewards=rewards,
    dones=dones
)


# -----------------------------
# Mostrar información
# -----------------------------

print()
print("Dataset generado correctamente.")
print(f"Archivo: {OUTPUT_FILE}")
print(f"Experiencias: {len(states)}")
print(f"States: {states.shape}")
print(f"Actions: {actions.shape}")
print(f"Next states: {next_states.shape}")
print(f"Rewards: {rewards.shape}")
print(f"Dones: {dones.shape}")