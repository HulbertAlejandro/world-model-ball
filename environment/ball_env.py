import numpy as np


class BallEnv:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.gravity = 0.5
        self.ball_radius = 10.0
        self.restitution = 0.9

        self.x = 0.0
        self.y = 0.0
        self.vx = 0.0
        self.vy = 0.0

    @property
    def ground_y(self):
        return self.height - self.ball_radius

    def reset(self):
        self.x = 100.0
        self.y = 100.0
        self.vx = 0.0
        self.vy = 0.0

        return self.get_state()

    def get_state(self):
        return np.array(
            [self.x, self.y, self.vx, self.vy],
            dtype=np.float32
        )

    def step(self):
        self.vy += self.gravity

        self.x += self.vx
        self.y += self.vy

        if self.y >= self.ground_y:
            self.y = self.ground_y
            self.vy = -self.vy * self.restitution

        return self.get_state()