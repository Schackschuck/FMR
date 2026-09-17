# ==========================
# TESTE SO DA GARRA
# ==========================
# Rode este programa sozinho para
# ajustar ABERTURA_GARRA e FORCA_GARRA
# antes de usar no percurso.

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port, Stop
from pybricks.tools import wait


hub = PrimeHub()

# Se abrir e fechar estiverem invertidos,
# troque para:
# Motor(Port.F, Direction.COUNTERCLOCKWISE)

motor_garra = Motor(Port.F)


VELOCIDADE_GARRA = 300
ABERTURA_GARRA = 90
FORCA_GARRA = 40


def calibrar_garra():

    print("Calibrando garra...")

    motor_garra.run_until_stalled(
        -VELOCIDADE_GARRA,
        then=Stop.COAST,
        duty_limit=FORCA_GARRA
    )

    motor_garra.reset_angle(0)

    wait(200)

    print("Garra calibrada.")


def abrir_garra():

    print("Abrindo garra...")

    motor_garra.run_target(
        VELOCIDADE_GARRA,
        ABERTURA_GARRA
    )

    motor_garra.stop()


def fechar_garra():

    print("Fechando garra...")

    motor_garra.run_until_stalled(
        -VELOCIDADE_GARRA,
        then=Stop.HOLD,
        duty_limit=FORCA_GARRA
    )


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

print("TESTE DA GARRA TERMINADO")
