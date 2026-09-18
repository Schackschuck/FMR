from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()


# ==========================================================
#        PERCURSO 2 - PASSOS 9 A 26 (COM O CANO)
# ==========================================================
# Segunda parte do percurso, com o
# CANO PESADO na garra.
#
# Roda na METADE da velocidade e
# FREIA DEVAGAR, para o robo nao
# empinar quando para.
#
# Antes de rodar: cano na garra,
# garra fechada, robo parado.


# ==========================
# SINAL DE INICIO
# ==========================

hub.light.on(Color.RED)

print("PERCURSO 2 - INICIANDO")


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
# METADE do percurso1, porque aqui
# o robo carrega o cano.

VELOCIDADE_RETA = 100     # mm por segundo
VELOCIDADE_GIRO = 50      # graus por segundo
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

ABERTURA_GARRA = 35


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

print("PERCURSO 2 INICIADO")


# ==========================
# 9 - ANDAR 100 CM
# ==========================

print("9) Andando 100 cm...")

andar(100)


# ==========================
# 10 - CURVA 90° DIREITA
# ==========================

print("10) Curva 90 graus direita")

girar_direita(90)


# ==========================
# 11 - ANDAR 5 CM
# ==========================

print("11) Andando 5 cm...")

andar(5)


# ==========================
# 12 - PARAR 1 SEGUNDO
# ==========================

print("12) Parado 1 segundo")

robo.stop()

wait(1000)


# ==========================
# 13 - ABRIR A GARRA 35°
# ==========================

print("13) Abrindo a garra")

abrir_garra()


# ==========================
# 14 - RÉ 5 CM
# ==========================

print("14) Dando re 5 cm...")

re(5)


# ==========================
# 15 - CURVA 90° DIREITA
# ==========================

print("15) Curva 90 graus direita")

girar_direita(90)


# ==========================
# 16 - ANDAR 100 CM
# ==========================

print("16) Andando 100 cm...")

andar(100)


# ==========================
# 17 - GIRO DE 180° DIREITA
# ==========================

print("17) Giro de 180 graus direita")

girar_direita(180)


# ==========================
# 18 - PARAR 10 SEGUNDOS
# ==========================

print("18) Parado 10 segundos")

robo.stop()

wait(10000)


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
# 21 - ANDAR 5 CM
# ==========================

print("21) Andando 5 cm...")

andar(5)


# ==========================
# 22 - ABRIR A GARRA 35°
# ==========================

print("22) Abrindo a garra")

abrir_garra()


# ==========================
# 23 - RÉ 5 CM
# ==========================

print("23) Dando re 5 cm...")

re(5)


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
print("PERCURSO 2 TERMINADO")
print("==========================")

wait(1000)
