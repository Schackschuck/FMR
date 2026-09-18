from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()


# ==========================================================
#        TESTE RAPIDO - 10 CM E GARRA 30 GRAUS
# ==========================================================
# Anda 10 cm para frente e abre a
# garra 30 graus. Só isso.
#
# Deixe 30 cm livres na frente do
# robo.

hub.light.on(Color.RED)

print("TESTE RAPIDO INICIADO")


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
# Deixe a garra fechada antes de
# iniciar o programa.

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

VELOCIDADE_RETA = 200     # mm por segundo
VELOCIDADE_GIRO = 100     # graus por segundo
VELOCIDADE_GARRA = 300    # graus por segundo


# ==========================
# O QUE VAI SER TESTADO
# ==========================

DISTANCIA_TESTE = 10      # cm
ABERTURA_GARRA = 80       # graus


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
# 1 - ANDAR 10 CM
# ==========================

hub.light.on(Color.GREEN)

print("Andando", DISTANCIA_TESTE, "cm...")

robo.straight(DISTANCIA_TESTE * 10)

robo.stop()

print("Desvio do rumo:", hub.imu.heading())

wait(1000)


# ==========================
# 2 - ABRIR A GARRA 30 GRAUS
# ==========================

print("Abrindo garra", ABERTURA_GARRA, "graus...")

motor_garra.run_angle(
    VELOCIDADE_GARRA,
    ABERTURA_GARRA
)

motor_garra.stop()

print("Angulo da garra:", motor_garra.angle())


# ==========================
# FIM
# ==========================

hub.light.on(Color.BLUE)

print("==========================")
print("TESTE TERMINADO")
print("==========================")

wait(1000)
