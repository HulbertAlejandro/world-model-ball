import numpy as np


DATASET_FILE = "data/ball_dataset.npz"


# -----------------------------
# Cargar dataset
# -----------------------------

data = np.load(DATASET_FILE)

states = data["states"]
actions = data["actions"]
next_states = data["next_states"]
rewards = data["rewards"]
dones = data["dones"]


# -----------------------------
# Información general
# -----------------------------

print("=== DATASET ===")
print(f"Experiencias: {len(states)}")
print()

print("Shapes:")
print(f"states:      {states.shape}")
print(f"actions:     {actions.shape}")
print(f"next_states: {next_states.shape}")
print(f"rewards:     {rewards.shape}")
print(f"dones:       {dones.shape}")
print()


# -----------------------------
# Distribución de acciones
# -----------------------------

print("=== ACCIONES ===")

for action in [0, 1, 2]:

    count = np.sum(actions == action)
    percentage = count / len(actions) * 100

    action_name = {
        0: "izquierda",
        1: "quieto",
        2: "derecha",
    }[action]

    print(
        f"{action} ({action_name}): "
        f"{count} ({percentage:.2f}%)"
    )

print()


# -----------------------------
# Distribución de rewards
# -----------------------------

print("=== REWARDS ===")

unique_rewards, counts = np.unique(
    rewards,
    return_counts=True
)

for reward, count in zip(unique_rewards, counts):

    percentage = count / len(rewards) * 100

    print(
        f"Reward {reward:5.1f}: "
        f"{count} ({percentage:.2f}%)"
    )

print()


# -----------------------------
# Episodios terminados
# -----------------------------

terminal_count = np.sum(dones)

print("=== EPISODIOS ===")
print(f"Transiciones terminales: {terminal_count}")
print()


# -----------------------------
# Estadísticas de los estados
# -----------------------------

state_names = [
    "x",
    "y",
    "vx",
    "vy",
    "paddle_x",
]

print("=== ESTADOS ===")

for i, name in enumerate(state_names):

    values = states[:, i]

    print(
        f"{name:8s} | "
        f"min={values.min():8.2f} | "
        f"max={values.max():8.2f} | "
        f"mean={values.mean():8.2f} | "
        f"std={values.std():8.2f}"
    )

print()


# -----------------------------
# Comprobar valores inválidos
# -----------------------------

print("=== VALIDACIÓN ===")

print(
    "NaN en states:",
    np.isnan(states).any()
)

print(
    "NaN en next_states:",
    np.isnan(next_states).any()
)

print(
    "NaN en rewards:",
    np.isnan(rewards).any()
)

print(
    "Acciones válidas:",
    np.all(np.isin(actions, [0, 1, 2]))
)