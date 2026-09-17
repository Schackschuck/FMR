from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


# ==========================
# HUB
# ==========================

hub = PrimeHub()


# ==========================
# MOTORES
# ==========================

motor_a = Motor(Port.A)
motor_b = Motor(Port.B)


# ==========================
# MOTOR DA GARRA
# ==========================
# Se a garra abrir quando deveria fechar,
# troque para:
# Motor(Port.F, Direction.COUNTERCLOCKWISE)

motor_garra = Motor(Port.F)


# ==========================
# MEDIDAS
# ==========================

DIAMETRO_RODA = 5.5       # cm


# ==========================
# VELOCIDADES
# ==========================

VELOCIDADE = 400
VELOCIDADE_GIRO = 200
VELOCIDADE_GARRA = 300


# ==========================
# AJUSTES DA GARRA
# ==========================

# Quanto o motor gira para abrir
# a garra (em graus)
ABERTURA_GARRA = 90

# Forca maxima da garra em %
# Valor baixo = aperta menos
# e nao trava o motor
FORCA_GARRA = 40


# ==========================
# FUNÇÃO PARA ANDAR PARA FRENTE
# ==========================

def andar(distancia_cm):

    circunferencia = 3.14159265 * DIAMETRO_RODA

    graus_motor = (
        distancia_cm / circunferencia
    ) * 360

    motor_a.run_angle(
        -VELOCIDADE,
        graus_motor,
        wait=False
    )

    motor_b.run_angle(
        VELOCIDADE,
        graus_motor
    )


# ==========================
# FUNÇÃO PARA DAR RÉ
# ==========================

def re(distancia_cm):

    circunferencia = 3.14159265 * DIAMETRO_RODA

    graus_motor = (
        distancia_cm / circunferencia
    ) * 360

    motor_a.run_angle(
        VELOCIDADE,
        graus_motor,
        wait=False
    )

    motor_b.run_angle(
        -VELOCIDADE,
        graus_motor
    )


# ==========================
# GIRO PARA A ESQUERDA
# COM GIROSCÓPIO
# ==========================

def girar_esquerda(angulo):

    print("Zerando giroscopio...")

    hub.imu.reset_heading(0)

    wait(200)

    print("Girando esquerda:", angulo)

    while True:

        heading = hub.imu.heading()

        print("Angulo:", heading)

        motor_a.run(VELOCIDADE_GIRO)
        motor_b.run(VELOCIDADE_GIRO)

        if abs(heading) >= angulo:
            break

        wait(5)

    motor_a.stop()
    motor_b.stop()

    wait(200)

    print("Giro terminado.")
    print("Angulo final:", hub.imu.heading())


# ==========================
# CALIBRAR A GARRA
# ==========================
# Fecha a garra devagar ate travar
# e usa esse ponto como ZERO.
# Rode isso uma vez no inicio do
# programa.

def calibrar_garra():

    print("Calibrando garra...")

    motor_garra.run_until_stalled(
        -VELOCIDADE_GARRA,
        then=Stop.COAST,
        duty_limit=FORCA_GARRA
    )

    motor_garra.reset_angle(0)

    wait(200)

    print("Garra calibrada. Zero definido.")


# ==========================
# ABRIR A GARRA
# ==========================

def abrir_garra():

    print("Abrindo garra...")

    motor_garra.run_target(
        VELOCIDADE_GARRA,
        ABERTURA_GARRA
    )

    motor_garra.stop()

    print("Garra aberta.")


# ==========================
# FECHAR A GARRA
# ==========================
# Fecha ate encostar no objeto
# e continua segurando (HOLD)

def fechar_garra():

    print("Fechando garra...")

    motor_garra.run_until_stalled(
        -VELOCIDADE_GARRA,
        then=Stop.HOLD,
        duty_limit=FORCA_GARRA
    )

    print("Garra fechada.")


# ==========================
# SOLTAR A GARRA
# ==========================
# Desliga o motor da garra para
# nao esquentar sem necessidade

def soltar_garra():

    motor_garra.stop()


# ==========================================================
#                    PREPARAÇÃO
# ==========================================================

calibrar_garra()

abrir_garra()


# ==========================================================
#                    PERCURSO 1
# ==========================================================

# 1 - ANDAR 2,10 METROS

print("PERCURSO 1")
print("Andando 2,10 metros...")

andar(210)


# 2 - PARAR 1 SEGUNDO

motor_a.stop()
motor_b.stop()

wait(1000)


# 3 - GIRAR 85° PARA ESQUERDA

print("Girando 85 graus para esquerda...")

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

motor_a.stop()
motor_b.stop()

wait(500)

fechar_garra()

wait(500)


# ==========================
# FIM DO PERCURSO 1
# ==========================

motor_a.stop()
motor_b.stop()

print("PERCURSO 1 TERMINADO")

wait(1000)


# ==========================================================
#                    PERCURSO DE VOLTA
# ==========================================================

# 6 - RÉ 50 CM

print("Dando re 50 cm...")

re(50)


# 7 - PARAR 1 SEGUNDO

motor_a.stop()
motor_b.stop()

wait(1000)


# 8 - GIRAR 90° PARA ESQUERDA
# CORRIGIDO

print("Girando 90 graus para esquerda...")

girar_esquerda(90)


# 9 - ANDAR 2,10 METROS

print("Andando 2,10 metros de volta...")

andar(210)


# ==========================
# FIM
# ==========================

motor_a.stop()
motor_b.stop()


# ==========================
# SOLTAR O OBJETO
# ==========================

wait(500)

abrir_garra()

wait(500)

soltar_garra()

print("==========================")
print("PERCURSO COMPLETO")
print("==========================")

wait(1000)
