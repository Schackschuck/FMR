from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

from pybricks.iodevices import XboxController


# ==========================================================
#          MISSAO 2 - CONTROLE PELO XBOX
# ==========================================================
# O robo e dirigido pelo controle do
# Xbox. So a tracao: motores A e B.
#
# Setas             = velocidade fixa
# Joystick ESQUERDO = ajuste fino,
#                     mais rapido
#                     quanto mais
#                     empurra
#
# Se usar os dois juntos, as setas
# mandam. Soltou tudo, o robo para.
#
# Antes de rodar: controle ligado.


# ==========================
# SINAL DE INICIO
# ==========================

hub.light.on(Color.RED)

print("MISSAO 2 - INICIANDO")


# ==========================
# MOTORES DA TRACAO
# ==========================

motor_esquerdo = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motor_direito = Motor(Port.B)


# ==========================
# MEDIDAS DO ROBO
# ==========================
# Em MILIMETROS

DIAMETRO_RODA = 55        # mm
DISTANCIA_RODAS = 143     # mm


# ==========================
# VELOCIDADES
# ==========================
# As setas andam sempre nessas
# velocidades. O joystick chega
# nelas quando empurrado ate o fim.

VELOCIDADE_RETA = 200     # mm por segundo
VELOCIDADE_GIRO = 100     # graus por segundo


# ==========================
# O ROBO
# ==========================

robo = DriveBase(
    motor_esquerdo,
    motor_direito,
    wheel_diameter=DIAMETRO_RODA,
    axle_track=DISTANCIA_RODAS
)

# SEM giroscopio, de proposito: aqui
# quem corrige o rumo e quem dirige.
# Com ele, os movimentos curtos davam
# trancos e o robo tremia parado.

robo.use_gyro(False)


# ==========================
# CONECTAR O CONTROLE
# ==========================
# Primeira vez com este hub: segure
# o botao de parear (atras do
# controle) ate o botao Xbox piscar
# rapido, e so entao rode o programa.

print("Procurando o controle...")

controle = XboxController()

print("Controle conectado.")


# ==========================
# COMANDOS
# ==========================

print("================================")
print("        MISSAO 2 - XBOX")
print("================================")

print("")
print("SETAS - velocidade fixa:")
print("Cima = FRENTE")
print("Baixo = RE")
print("Esquerda / direita = GIRAR")

print("")
print("JOYSTICK ESQUERDO - ajuste fino:")
print("Empurrar pouco = devagar")

print("")
print("Soltou tudo, o robo para.")


# ==========================================================
#                      CONTROLE
# ==========================================================

hub.light.on(Color.GREEN)

while True:

    # ==========================
    # SETAS
    # ==========================
    # Da para apertar duas juntas:
    # cima com direita anda fazendo
    # curva.

    botoes = controle.buttons.pressed()

    velocidade = 0
    giro = 0

    if Button.UP in botoes:

        velocidade = VELOCIDADE_RETA

    elif Button.DOWN in botoes:

        velocidade = -VELOCIDADE_RETA

    if Button.RIGHT in botoes:

        giro = VELOCIDADE_GIRO

    elif Button.LEFT in botoes:

        giro = -VELOCIDADE_GIRO


    # ==========================
    # JOYSTICK ESQUERDO
    # ==========================
    # So vale com nenhuma seta
    # apertada. De -100 a 100:
    # cima e direita sao positivos.

    if velocidade == 0 and giro == 0:

        lado, frente = controle.joystick_left()

        velocidade = frente * VELOCIDADE_RETA / 100
        giro = lado * VELOCIDADE_GIRO / 100


    # ==========================
    # ANDAR OU PARAR
    # ==========================

    if velocidade == 0 and giro == 0:

        # Nada apertado: freia as rodas
        # sem ficar segurando o robo, entao
        # nao tem barulho nem tranco.
        robo.brake()

    else:

        robo.drive(velocidade, giro)


    wait(10)
