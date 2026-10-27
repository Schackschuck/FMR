from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()


# ==========================================================
#              TESTE SO DA GARRA - PORTA D
# ==========================================================
# Este programa NAO anda. So mexe na
# garra, para achar o sentido certo
# e a abertura certa.

hub.light.on(Color.RED)

print("==============================")
print("TESTE DA GARRA")
print("==============================")


# ==========================
# MOTOR DA GARRA
# ==========================
# Depois da mudanca na estrutura, o
# sentido voltou ao normal: CLOCKWISE.
# Positivo continua sendo ABRIR.

motor_garra = Motor(Port.D, Direction.CLOCKWISE)


# A posicao em que a garra esta
# AGORA vale como angulo ZERO.
# Deixe a garra fechada antes de
# iniciar o programa.

motor_garra.reset_angle(0)


# ==========================
# AJUSTES
# ==========================

VELOCIDADE_GARRA = 300

# Quanto o motor gira para abrir
# ou fechar (em graus)
ABERTURA_GARRA = 100


# ==========================
# ABRIR A GARRA
# ==========================

def abrir_garra():

    print("Abrindo...")

    motor_garra.run_angle(
        VELOCIDADE_GARRA,
        ABERTURA_GARRA
    )

    print("Angulo:", motor_garra.angle())


# ==========================
# FECHAR A GARRA
# ==========================

def fechar_garra():

    print("Fechando...")

    motor_garra.run_angle(
        VELOCIDADE_GARRA,
        -ABERTURA_GARRA
    )

    print("Angulo:", motor_garra.angle())


# ==========================================================
#                 PARTE 1 - AUTOMATICO
# ==========================================================

hub.light.on(Color.GREEN)

print("------------------------------")
print("AUTOMATICO: 3 ciclos")

for i in range(3):

    print("Ciclo", i + 1, "de 3")

    abrir_garra()
    wait(1000)

    fechar_garra()
    wait(1000)

motor_garra.stop()

print("Automatico terminado.")


# ==========================================================
#                 PARTE 2 - MANUAL
# ==========================================================
# Controle pelos botoes de seta
# do hub.

hub.light.on(Color.BLUE)

print("==============================")
print("MODO MANUAL")
print("Seta ESQUERDA  = fechar")
print("Seta DIREITA   = abrir")
print("Botao CENTRAL  = encerrar")
print("==============================")

while True:

    botoes = hub.buttons.pressed()

    if Button.LEFT in botoes:

        fechar_garra()

        wait(300)

    if Button.RIGHT in botoes:

        abrir_garra()

        wait(300)

    wait(50)
