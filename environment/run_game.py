import pygame

from environment.ball_env import BallEnv


# -----------------------------
# Configuración
# -----------------------------

FPS = 60

BACKGROUND = (30, 30, 30)
BALL_COLOR = (255, 255, 255)
PADDLE_COLOR = (80, 180, 255)
TEXT_COLOR = (220, 220, 220)


# -----------------------------
# Inicializar Pygame
# -----------------------------

pygame.init()

env = BallEnv()

screen = pygame.display.set_mode(
    (env.width, env.height)
)

pygame.display.set_caption(
    "World Model Ball - Entorno"
)

clock = pygame.time.Clock()

font = pygame.font.Font(None, 28)


# -----------------------------
# Estado inicial
# -----------------------------

state = env.reset()

reward = 0.0

running = True


# -----------------------------
# Bucle principal
# -----------------------------

while running:

    # -------------------------
    # Eventos
    # -------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            elif event.key == pygame.K_r:
                state = env.reset()


    # -------------------------
    # Leer teclado
    # -------------------------

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        action = 0

    elif keys[pygame.K_RIGHT]:
        action = 2

    else:
        action = 1


    # -------------------------
    # Actualizar entorno
    # -------------------------

    if not env.done:
        state, reward, done = env.step(action)


    # -------------------------
    # Dibujar
    # -------------------------

    screen.fill(BACKGROUND)

    # Bola
    pygame.draw.circle(
        screen,
        BALL_COLOR,
        (
            int(env.x),
            int(env.y)
        ),
        int(env.ball_radius)
    )

    # Plataforma
    paddle_rect = pygame.Rect(
        int(env.paddle_left),
        int(env.paddle_y),
        int(env.paddle_width),
        int(env.paddle_height)
    )

    pygame.draw.rect(
        screen,
        PADDLE_COLOR,
        paddle_rect
    )

    # Información
    info = font.render(
        f"Pasos: {env.step_count}   "
        f"Reward: {reward if not env.done else -10.0}",
        True,
        TEXT_COLOR
    )

    screen.blit(
        info,
        (10, 10)
    )

    # Mensaje de derrota
    if env.done:

        game_over = font.render(
            "PERDISTE - Presiona R para reiniciar",
            True,
            TEXT_COLOR
        )

        screen.blit(
            game_over,
            (
                10,
                45
            )
        )

    pygame.display.flip()

    clock.tick(FPS)


# -----------------------------
# Cerrar Pygame
# -----------------------------

pygame.quit()