from openrdk import CommsRuntime
from openrdk import Motors

VELOCIDADE = 30

runtime = CommsRuntime(
    auto_start=True,
    enable_webview=True,
    enable_webview_updates=True,
)

motor_r = runtime.traction("98:3D:AE:43:50:50")
motor_l = runtime.traction("10:20:BA:AA:E7:28")

motores = Motors(right=motor_r, left=motor_l)

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
            motores.left.move(VELOCIDADE)
            motores.right.move(VELOCIDADE)

        elif comando == "s":
            motores.left.move(-VELOCIDADE)
            motores.right.move(-VELOCIDADE)

        elif comando == "a":
            motores.left.move(-VELOCIDADE)
            motores.right.move(VELOCIDADE)

        elif comando == "d":
            motores.left.move(VELOCIDADE)
            motores.right.move(-VELOCIDADE)

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
