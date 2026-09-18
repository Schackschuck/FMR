from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()


# ==========================================================
#          PERCURSO 1 - PASSOS 1 A 7 (SEM O CANO)
# ==========================================================
# Primeira parte do percurso, com o
# robo VAZIO, na velocidade normal.
#
# Termina no ponto onde o cano e
# colocado na garra. Depois disso,
# rode o percurso2.py.


# ==========================
# SINAL DE INICIO
# ==========================

hub.light.on(Color.RED)

print("PERCURSO 1 - INICIANDO")


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
# Robo vazio: velocidade normal

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

robo.use_gyro(True)

robo.settings(
    straight_speed=VELOCIDADE_RETA,
    turn_rate=VELOCIDADE_GIRO
)


# ==========================
# ESPERAR O GIROSCOPIO
# ==========================
# NAO mexa no robo agora.

print("Preparando giroscopio...")

while not hub.imu.ready():
    wait(10)

hub.imu.reset_heading(0)

print("Giroscopio pronto.")


# ==========================
# FUNÇÃO PARA ANDAR PARA FRENTE
# ==========================

def andar(distancia_cm):

    robo.straight(distancia_cm * 10)


# ==========================
# FUNÇÃO PARA DAR RÉ
# ==========================

def re(distancia_cm):

    robo.straight(-distancia_cm * 10)


# ==========================
# GIRO PARA A ESQUERDA
# ==========================
# No Pybricks, angulo NEGATIVO
# gira para a esquerda.

def girar_esquerda(angulo):

    print("Girando esquerda:", angulo)

    robo.turn(-angulo)

    print("Angulo do hub:", hub.imu.heading())


# ==========================
# GIRO PARA A DIREITA
# ==========================

def girar_direita(angulo):

    print("Girando direita:", angulo)

    robo.turn(angulo)

    print("Angulo do hub:", hub.imu.heading())


# ==========================================================
#                      PERCURSO
# ==========================================================

hub.light.on(Color.GREEN)

print("PERCURSO 1 INICIADO")


# ==========================
# 1 - ANDAR 2,10 METROS
# ==========================

print("1) Andando 2,10 metros...")

andar(210)


# ==========================
# 2 - CURVA 90° ESQUERDA
# ==========================

print("2) Curva 90 graus esquerda")

girar_esquerda(90)


# ==========================
# 3 - ANDAR 60 CM
# ==========================

print("3) Andando 60 cm...")

andar(60)


# ==========================
# 4 - PARAR 1 SEGUNDO
# ==========================

print("4) Parado 1 segundo")

robo.stop()

wait(1000)


# ==========================
# 5 - RÉ 37 CM
# ==========================

print("5) Dando re 37 cm...")

re(37)


# ==========================
# 6 - CURVA 90° ESQUERDA
# ==========================

print("6) Curva 90 graus esquerda")

girar_esquerda(90)


# ==========================
# 7 - ANDAR 2,10 METROS
# ==========================

print("7) Andando 2,10 metros...")

andar(210)


# ==========================
# FIM DA PARTE 1
# ==========================

robo.stop()

hub.light.on(Color.BLUE)

print("==========================")
print("PERCURSO 1 TERMINADO")
print("Coloque o cano na garra e")
print("rode o percurso2.py")
print("==========================")

wait(1000)
