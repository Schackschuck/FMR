from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()


# ==========================
# SINAL DE QUE O PROGRAMA
# COMECOU
# ==========================
# Luz VERMELHA + bip = o programa
# esta rodando de verdade.
# Se nao acender nada, o problema
# nao esta no codigo: o programa
# nao foi baixado ou nao foi
# iniciado no hub.

hub.light.on(Color.RED)
hub.speaker.beep(500, 200)

print("PROGRAMA INICIADO")


# ==========================
# MOTORES DA TRACAO
# ==========================

motor_a = Motor(Port.A)
motor_b = Motor(Port.B)

print("Motores A e B: OK")


# ==========================
# MOTOR DA GARRA
# ==========================
# Se a garra nao estiver ligada na
# porta F, o programa AVISA e segue
# sem ela, em vez de travar.
#
# Se a garra abrir quando deveria
# fechar, troque para:
# Motor(Port.F, Direction.COUNTERCLOCKWISE)

try:

    motor_garra = Motor(Port.F)

    TEM_GARRA = True

    print("Garra na porta F: OK")

except OSError:

    motor_garra = None

    TEM_GARRA = False

    print("AVISO: nada ligado na porta F")
    print("O percurso vai rodar SEM a garra")


# ==========================
# MEDIDAS
# ==========================

DIAMETRO_RODA = 5.5       # cm


# ==========================
# VELOCIDADES
# ==========================

VELOCIDADE = 400
VELOCIDADE_GIRO = 200


# ==========================
# AJUSTES DA GARRA
# ==========================

# Quanto o motor gira para abrir
# a garra (em graus)
ABERTURA_GARRA = 90

# Forca da garra em %
# Valor baixo = aperta menos
FORCA_GARRA = 40

# Tempo maximo que a garra pode
# ficar tentando abrir ou fechar.
# Isso impede o programa de travar
# para sempre.
TEMPO_LIMITE_GARRA = 3000   # ms


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
# FECHAR A GARRA
# ==========================
# Fecha ate encostar no objeto e
# para sozinha. Nunca fica travada:
# se passar do TEMPO_LIMITE_GARRA
# ela desiste e o programa segue.

def fechar_garra():

    if not TEM_GARRA:
        print("Sem garra. Pulando fechar.")
        return

    print("Fechando garra...")

    relogio = StopWatch()

    motor_garra.dc(-FORCA_GARRA)

    while relogio.time() < TEMPO_LIMITE_GARRA:

        parou = abs(motor_garra.speed()) < 30

        if relogio.time() > 300 and parou:
            break

        wait(10)

    motor_garra.hold()

    print("Garra fechada.")


# ==========================
# ABRIR A GARRA
# ==========================

def abrir_garra():

    if not TEM_GARRA:
        print("Sem garra. Pulando abrir.")
        return

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

    print("Garra aberta.")


# ==========================
# CALIBRAR A GARRA
# ==========================
# Fecha a garra ate o fim e usa
# esse ponto como ZERO.

def calibrar_garra():

    if not TEM_GARRA:
        print("Sem garra. Pulando calibracao.")
        return

    print("Calibrando garra...")

    fechar_garra()

    motor_garra.reset_angle(0)

    motor_garra.stop()

    wait(200)

    print("Garra calibrada. Zero definido.")


# ==========================
# SOLTAR A GARRA
# ==========================
# Desliga o motor da garra

def soltar_garra():

    if not TEM_GARRA:
        return

    motor_garra.stop()


# ==========================================================
#                    PREPARAÇÃO
# ==========================================================

calibrar_garra()

abrir_garra()


# ==========================================================
#                    PERCURSO 1
# ==========================================================

# Luz VERDE = saiu da preparacao
# e comecou a andar

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
