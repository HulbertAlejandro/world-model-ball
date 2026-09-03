import numpy as np


class BallEnv:
    def __init__(self):
        # Dimensiones del entorno
        self.width = 800
        self.height = 600

        # Física de la bola
        self.gravity = 0.5
        self.ball_radius = 10.0
        self.restitution = 0.9

        # Plataforma
        self.paddle_width = 120.0
        self.paddle_height = 20.0
        self.paddle_speed = 8.0

        # Estado de la bola
        self.x = 0.0
        self.y = 0.0
        self.vx = 0.0
        self.vy = 0.0

        # Estado de la plataforma
        self.paddle_x = 0.0

        # Estado del episodio
        self.done = False
        self.step_count = 0

    @property
    def ground_y(self):
        return self.height - self.ball_radius

    @property
    def left_wall_x(self):
        return self.ball_radius

    @property
    def right_wall_x(self):
        return self.width - self.ball_radius

    @property
    def paddle_y(self):
        return self.height - 60.0

    @property
    def paddle_left(self):
        return self.paddle_x - self.paddle_width / 2

    @property
    def paddle_right(self):
        return self.paddle_x + self.paddle_width / 2

    def reset(self):
        self.x = 400.0
        self.y = 200.0
        self.vx = 3.0
        self.vy = 0.0

        self.paddle_x = self.width / 2

        self.done = False
        self.step_count = 0

        return self.get_state()

    def get_state(self):
        return np.array(
            [
                self.x,
                self.y,
                self.vx,
                self.vy,
                self.paddle_x,
            ],
            dtype=np.float32
        )

    def step(self, action):
        # No permitir avanzar un episodio terminado
        if self.done:
            raise RuntimeError(
                "El episodio ha terminado. Debes llamar a reset()."
            )

        # Validar acción
        if action not in (0, 1, 2):
            raise ValueError("La acción debe ser 0, 1 o 2.")

        self.step_count += 1

        # --------------------------------
        # 1. Mover la plataforma
        # --------------------------------

        if action == 0:
            self.paddle_x -= self.paddle_speed

        elif action == 2:
            self.paddle_x += self.paddle_speed

        # action == 1 significa quedarse quieto

        # Limitar plataforma a las paredes
        half_width = self.paddle_width / 2

        self.paddle_x = np.clip(
            self.paddle_x,
            half_width,
            self.width - half_width
        )

        # --------------------------------
        # 2. Actualizar física de la bola
        # --------------------------------

        self.vy += self.gravity

        self.x += self.vx
        self.y += self.vy

        reward = 0.0

        # --------------------------------
        # 3. Colisión con paredes
        # --------------------------------

        if self.x <= self.left_wall_x:
            self.x = self.left_wall_x
            self.vx = -self.vx * self.restitution

        if self.x >= self.right_wall_x:
            self.x = self.right_wall_x
            self.vx = -self.vx * self.restitution

        # --------------------------------
        # 4. Colisión con plataforma
        # --------------------------------

        if (
            self.vy > 0
            and self.y + self.ball_radius >= self.paddle_y
            and self.y - self.ball_radius <= self.paddle_y + self.paddle_height
            and self.paddle_left <= self.x <= self.paddle_right
        ):
            self.y = self.paddle_y - self.ball_radius
            self.vy = -abs(self.vy) * self.restitution

            reward = 1.0

        # --------------------------------
        # 5. Bola perdida
        # --------------------------------

        if self.y - self.ball_radius > self.height:
            reward = -10.0
            self.done = True

        return self.get_state(), reward, self.done