from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()


# ==========================
# SINAL DE INICIO
# ==========================
# Luz VERMELHA = o programa
# esta rodando

hub.light.on(Color.RED)

print("PROGRAMA INICIADO")


# ==========================
# MOTORES DA TRACAO
# ==========================
# O motor da ESQUERDA e invertido
# para que os dois andem para
# frente com valor positivo.
# Isso e o que o DriveBase espera.

motor_esquerdo = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motor_direito = Motor(Port.B)


# ==========================
# MOTOR DA GARRA
# ==========================
# O sentido esta invertido no robo,
# por isso o COUNTERCLOCKWISE.
# Assim positivo continua sendo ABRIR.

motor_garra = Motor(Port.D, Direction.COUNTERCLOCKWISE)


# A posicao em que a garra esta
# AGORA vale como angulo ZERO.
# Deixe a garra fechada antes de
# iniciar o programa.

motor_garra.reset_angle(0)


# ==========================
# MEDIDAS DO ROBO
# ==========================
# ATENCAO: em MILIMETROS, que e o
# que o DriveBase usa.

# Diametro da roda
DIAMETRO_RODA = 55        # mm

# Distancia de UM CENTRO DE RODA
# ate o outro, medida no robo.
DISTANCIA_RODAS = 143     # mm


# ==========================
# VELOCIDADES
# ==========================

VELOCIDADE_RETA = 200     # mm por segundo
VELOCIDADE_GIRO = 100     # graus por segundo
VELOCIDADE_GARRA = 300    # graus por segundo


# ==========================
# AJUSTES DA GARRA
# ==========================

# Quanto o motor gira para abrir
# ou fechar a garra (em graus)
ABERTURA_GARRA = 35


# ==========================
# O ROBO
# ==========================
# O DriveBase controla os dois
# motores juntos. Ele iguala as
# rodas sozinho, entao o robo
# anda reto.

robo = DriveBase(
    motor_esquerdo,
    motor_direito,
    wheel_diameter=DIAMETRO_RODA,
    axle_track=DISTANCIA_RODAS
)


# ==========================
# GIROSCOPIO LIGADO
# ==========================
# Esta linha e a que segura a linha
# reta de verdade: o robo mede o
# proprio desvio e corrige enquanto
# anda.

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
#                    PREPARAÇÃO
# ==========================================================

abrir_garra()


# ==========================================================
#                    PERCURSO 1
# ==========================================================

# Luz VERDE = comecou a andar

hub.light.on(Color.GREEN)


# 1 - ANDAR 2,10 METROS

print("PERCURSO 1")
print("Andando 2,10 metros...")

andar(210)


# 2 - PARAR 1 SEGUNDO

robo.stop()

wait(1000)


# 3 - GIRAR 85° PARA ESQUERDA

girar_esquerda(85)


# 4 - ANDAR 60 CM

print("Andando 60 cm...")

andar(60)


# ==========================
# 5 - PEGAR O OBJETO
# ==========================
# Se a garra tiver que fechar em
# outro ponto, mova esta chamada
# de lugar (ela e so uma linha).

robo.stop()

wait(500)

fechar_garra()

wait(500)


# ==========================
# FIM DO PERCURSO 1
# ==========================

print("PERCURSO 1 TERMINADO")

wait(1000)


# ==========================================================
#                    PERCURSO DE VOLTA
# ==========================================================

# 6 - RÉ 50 CM

print("Dando re 50 cm...")

re(50)


# 7 - PARAR 1 SEGUNDO

robo.stop()

wait(1000)


# 8 - GIRAR 90° PARA ESQUERDA

girar_esquerda(90)


# 9 - ANDAR 2,10 METROS

print("Andando 2,10 metros de volta...")

andar(210)


# ==========================
# FIM
# ==========================

robo.stop()


# ==========================
# SOLTAR O OBJETO
# ==========================

wait(500)

abrir_garra()

wait(500)

soltar_garra()


# Luz AZUL = terminou tudo

hub.light.on(Color.BLUE)

print("==========================")
print("PERCURSO COMPLETO")
print("==========================")

wait(1000)
