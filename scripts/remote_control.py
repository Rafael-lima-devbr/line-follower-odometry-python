from openrdk import CommsRuntime
from openrdk import Motors
import time

VELOCIDADE_MAX = 60
PASSO = 2.5
TEMPO_ACELERACAO = 0.1

runtime = CommsRuntime(
    auto_start=True,
    enable_webview=True,
    enable_webview_updates=True,
)

motor_r = runtime.traction("98:3D:AE:43:50:50")
motor_l = runtime.traction("10:20:BA:AA:E7:28")

motores = Motors(right=motor_r, left=motor_l)


def acelerar(direcao):
    velocidade = 0

    while velocidade < VELOCIDADE_MAX:
        velocidade += PASSO

        if velocidade > VELOCIDADE_MAX:
            velocidade = VELOCIDADE_MAX

        motores.left.move(velocidade * direcao)
        motores.right.move(velocidade * direcao)

        time.sleep(TEMPO_ACELERACAO)


print("=== Controle Manual ===")
print("w = frente")
print("s = ré")
print("a = esquerda")
print("d = direita")
print("x = parar")
print("q = sair")

try:
    while True:
        comando = input("> ").strip().lower()

        if comando == "w":
            acelerar(1)

        elif comando == "s":
            acelerar(-1)

        elif comando == "a":
            motores.left.move(VELOCIDADE_MAX)
            motores.right.move(-VELOCIDADE_MAX)

        elif comando == "d":
            motores.left.move(-VELOCIDADE_MAX)
            motores.right.move(VELOCIDADE_MAX)

        elif comando == "x":
            motores.left.move(0)
            motores.right.move(0)

        elif comando == "q":
            motores.left.move(0)
            motores.right.move(0)
            break

        else:
            print("Comando inválido!")

finally:
    motores.left.move(0)
    motores.right.move(0)
