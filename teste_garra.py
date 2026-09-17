# ==========================
# TESTE SO DA GARRA
# ==========================
# Rode este programa sozinho para
# ajustar ABERTURA_GARRA e FORCA_GARRA
# antes de usar no percurso.

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Color, Direction, Port
from pybricks.tools import wait, StopWatch


hub = PrimeHub()

hub.light.on(Color.RED)
hub.speaker.beep(500, 200)

print("TESTE DA GARRA INICIADO")


# Se abrir e fechar estiverem
# invertidos, troque para:
# Motor(Port.F, Direction.COUNTERCLOCKWISE)

try:

    motor_garra = Motor(Port.F)

    print("Garra encontrada na porta F")

except OSError:

    print("ERRO: nada ligado na porta F")
    print("Confira o cabo antes de seguir.")

    raise


ABERTURA_GARRA = 90
FORCA_GARRA = 40
TEMPO_LIMITE_GARRA = 3000


def fechar_garra():

    print("Fechando garra...")

    relogio = StopWatch()

    motor_garra.dc(-FORCA_GARRA)

    while relogio.time() < TEMPO_LIMITE_GARRA:

        parou = abs(motor_garra.speed()) < 30

        if relogio.time() > 300 and parou:
            break

        wait(10)

    motor_garra.hold()

    print("Fechou em:", motor_garra.angle())


def abrir_garra():

    print("Abrindo garra...")

    relogio = StopWatch()

    motor_garra.dc(FORCA_GARRA)

    while relogio.time() < TEMPO_LIMITE_GARRA:

        if motor_garra.angle() >= ABERTURA_GARRA:
            break

        parou = abs(motor_garra.speed()) < 30

        if relogio.time() > 300 and parou:
            break

        wait(10)

    motor_garra.stop()

    print("Abriu em:", motor_garra.angle())


def calibrar_garra():

    print("Calibrando garra...")

    fechar_garra()

    motor_garra.reset_angle(0)

    motor_garra.stop()

    wait(200)

    print("Garra calibrada.")


# ==========================
# TESTE
# ==========================

calibrar_garra()

for i in range(3):

    print("Ciclo:", i + 1)

    abrir_garra()
    wait(1000)

    fechar_garra()
    wait(1000)

motor_garra.stop()

hub.light.on(Color.BLUE)

print("TESTE DA GARRA TERMINADO")
