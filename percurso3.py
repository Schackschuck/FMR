from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()


# ==========================================================
#     PERCURSO 3 - PASSOS 19 A 26 (SEGUNDO CANO)
# ==========================================================
# Leva o SEGUNDO cano, solta ele e
# volta.
#
# Anda rapido, mas FREIA DEVAGAR,
# para o robo nao empinar quando
# para com o peso do cano.
#
# Antes de rodar: cano na garra,
# garra fechada no cano, robo parado
# no lugar onde o percurso2 terminou.


# ==========================
# SINAL DE INICIO
# ==========================

hub.light.on(Color.RED)

print("PERCURSO 3 - INICIANDO")


# ==========================
# MOTORES DA TRACAO
# ==========================

motor_esquerdo = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motor_direito = Motor(Port.B)


# ==========================
# MOTOR DA GARRA
# ==========================

motor_garra = Motor(Port.D, Direction.CLOCKWISE)


# A posicao em que a garra esta
# AGORA vale como angulo ZERO.
# Ela deve estar fechada no cano.

motor_garra.reset_angle(0)


# ==========================
# MEDIDAS DO ROBO
# ==========================
# Em MILIMETROS

DIAMETRO_RODA = 55        # mm
DISTANCIA_RODAS = 143     # mm


# ==========================
# VELOCIDADES
# ==========================
# Mesma velocidade do percurso1.
# O que segura o cano nao e a
# velocidade, e o freio suave
# logo abaixo.

VELOCIDADE_RETA = 350     # mm por segundo
VELOCIDADE_GIRO = 150     # graus por segundo
VELOCIDADE_GARRA = 300    # graus por segundo


# ==========================
# ACELERACAO E FREIO
# ==========================
# Acelera normal, mas FREIA DEVAGAR.
# E a frenagem brusca que joga o
# peso do cano para frente e faz o
# robo empinar.

ACELERACAO_RETA = 250     # mm/s2
DESACELERACAO_RETA = 60   # mm/s2

ACELERACAO_GIRO = 300     # graus/s2
DESACELERACAO_GIRO = 100  # graus/s2


# ==========================
# AJUSTES DA GARRA
# ==========================

ABERTURA_GARRA = 100


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


# A tupla e (acelerar, desacelerar).
# O segundo valor e o freio.

robo.settings(
    straight_speed=VELOCIDADE_RETA,
    straight_acceleration=(
        ACELERACAO_RETA,
        DESACELERACAO_RETA
    ),
    turn_rate=VELOCIDADE_GIRO,
    turn_acceleration=(
        ACELERACAO_GIRO,
        DESACELERACAO_GIRO
    )
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


# ==========================
# ABRIR A GARRA
# ==========================

def abrir_garra():

    print("Abrindo garra...")

    motor_garra.run_angle(
        VELOCIDADE_GARRA,
        ABERTURA_GARRA
    )

    print("Garra aberta.")


# ==========================
# FECHAR A GARRA
# ==========================

def fechar_garra():

    print("Fechando garra...")

    motor_garra.run_angle(
        VELOCIDADE_GARRA,
        -ABERTURA_GARRA
    )

    print("Garra fechada.")


# ==========================
# SOLTAR A GARRA
# ==========================
# Desliga o motor da garra

def soltar_garra():

    motor_garra.stop()


# ==========================================================
#                      PERCURSO
# ==========================================================

hub.light.on(Color.GREEN)

print("PERCURSO 3 INICIADO")


# ==========================
# 19 - ANDAR 1,60 METROS
# ==========================

print("19) Andando 1,60 metros...")

andar(160)


# ==========================
# 20 - CURVA 90° DIREITA
# ==========================

print("20) Curva 90 graus direita")

girar_direita(90)


# ==========================
# 21 - ANDAR 14 CM
# ==========================

print("21) Andando 14 cm...")

andar(14)


# ==========================
# 22 - SOLTAR O CANO
# ==========================
# Abre a garra e deixa o cano.

print("22) Abrindo a garra")

abrir_garra()


# ==========================
# 23 - RÉ 14 CM
# ==========================

print("23) Dando re 14 cm...")

re(14)


# ==========================
# 24 - CURVA 90° DIREITA
# ==========================

print("24) Curva 90 graus direita")

girar_direita(90)


# ==========================
# 25 - VOLTAR 1,60 METROS
# ==========================

print("25) Voltando 1,60 metros...")

andar(160)


# ==========================
# 26 - PARAR
# ==========================

robo.stop()

soltar_garra()

hub.light.on(Color.BLUE)

print("==========================")
print("PERCURSO 3 TERMINADO")
print("==========================")

wait(1000)
