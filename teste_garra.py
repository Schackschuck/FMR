# ==========================================================
#              TESTE SO DA GARRA - PORTA F
# ==========================================================
# Este programa NAO anda. So mexe na
# garra, para voce achar o sentido
# certo, a abertura certa e a forca
# certa antes de rodar o percurso.
#
# Pode deixar o robo em cima da mesa.

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.tools import wait, StopWatch


# ==========================
# HUB
# ==========================

hub = PrimeHub()

hub.light.on(Color.RED)
hub.speaker.beep(500, 200)

print("==============================")
print("TESTE DA GARRA")
print("==============================")


# ==========================
# MOTOR DA GARRA
# ==========================
# Se a garra ABRIR quando deveria
# FECHAR, troque a linha por:
# Motor(Port.F, Direction.COUNTERCLOCKWISE)

try:

    motor_garra = Motor(Port.F)

    print("Garra encontrada na porta F")

except OSError:

    hub.light.on(Color.ORANGE)
    hub.speaker.beep(200, 800)

    print("ERRO: nada ligado na porta F")
    print("Confira o cabo e a porta.")

    raise


# ==========================
# AJUSTES
# ==========================

# Quanto o motor gira para abrir
ABERTURA_GARRA = 90

# Forca da garra em %
FORCA_GARRA = 40

# Tempo maximo de cada movimento.
# Impede o programa de travar.
TEMPO_LIMITE = 3000   # ms


# ==========================
# FECHAR A GARRA
# ==========================

def fechar_garra():

    print("Fechando...")

    relogio = StopWatch()

    motor_garra.dc(-FORCA_GARRA)

    while relogio.time() < TEMPO_LIMITE:

        parou = abs(motor_garra.speed()) < 30

        if relogio.time() > 300 and parou:
            break

        wait(10)

    motor_garra.hold()

    print("Fechou. Angulo:", motor_garra.angle())


# ==========================
# ABRIR A GARRA
# ==========================

def abrir_garra():

    print("Abrindo...")

    relogio = StopWatch()

    motor_garra.dc(FORCA_GARRA)

    while relogio.time() < TEMPO_LIMITE:

        if motor_garra.angle() >= ABERTURA_GARRA:
            break

        parou = abs(motor_garra.speed()) < 30

        if relogio.time() > 300 and parou:
            break

        wait(10)

    motor_garra.stop()

    print("Abriu. Angulo:", motor_garra.angle())


# ==========================
# CALIBRAR
# ==========================
# Fecha ate o fim e chama esse
# ponto de ZERO.

def calibrar_garra():

    print("------------------------------")
    print("Calibrando...")

    fechar_garra()

    motor_garra.reset_angle(0)

    motor_garra.stop()

    wait(200)

    print("Zero definido.")


# ==========================================================
#                 PARTE 1 - TESTE AUTOMATICO
# ==========================================================

calibrar_garra()

hub.light.on(Color.GREEN)

print("------------------------------")
print("TESTE AUTOMATICO: 3 ciclos")

for i in range(3):

    print("Ciclo", i + 1, "de 3")

    abrir_garra()
    wait(1000)

    fechar_garra()
    wait(1000)

motor_garra.stop()

print("Teste automatico terminado.")


# ==========================================================
#                 PARTE 2 - TESTE MANUAL
# ==========================================================
# Agora voce controla com os botoes
# de seta do hub.

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
