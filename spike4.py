from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()


# ==========================
# SINAL DE INICIO
# ==========================
# Luz VERMELHA + bip = o programa
# esta rodando

hub.light.on(Color.RED)
hub.speaker.beep(500, 200)

print("PROGRAMA INICIADO")


# ==========================
# MOTORES
# ==========================

motor_a = Motor(Port.A)
motor_b = Motor(Port.B)


# ==========================
# MOTOR DA GARRA
# ==========================
# Se a garra abrir quando deveria
# fechar, troque para:
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
# ou fechar a garra (em graus)
ABERTURA_GARRA = 90


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


# Luz AZUL = terminou tudo

hub.light.on(Color.BLUE)

print("==========================")
print("PERCURSO COMPLETO")
print("==========================")

wait(1000)
