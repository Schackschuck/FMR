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
# Setas = velocidade fixa, com o
#         giroscopio corrigindo os
#         desvios no meio do caminho.
#
# Soltou tudo, o robo para.
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
#
# DISTANCIA_RODAS e 128 so neste
# programa, de proposito: os outros
# continuam com 143.

DIAMETRO_RODA = 55        # mm
DISTANCIA_RODAS = 128     # mm


# ==========================
# VELOCIDADES
# ==========================
# As setas andam sempre nessas
# velocidades.

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

# COM giroscopio, de proposito: nesta
# missao ele corrige os desvios no
# meio do caminho. Parado, o robo
# fica solto (brake), para nao tremer
# nem dar tranco.

robo.use_gyro(True)

# O giroscopio so calibra com o robo
# PARADO: nao mexa nele ate liberar.

print("Calibrando o giroscopio...")

while not hub.imu.ready():

    wait(10)

print("Giroscopio pronto.")


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
print("O giroscopio corrige o rumo.")

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
    # ANDAR OU PARAR
    # ==========================

    if velocidade == 0 and giro == 0:

        # Nada apertado: freia as rodas
        # sem ficar segurando o robo, entao
        # nao tem barulho nem tranco. Nao
        # usar drive(0, 0): com o giroscopio
        # ele segura o robo o tempo todo.
        robo.brake()

    else:

        robo.drive(velocidade, giro)


    wait(10)
