from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

from pybricks.iodevices import XboxController


# ==========================================================
#             CONTROLE DO ROBO PELO XBOX
# ==========================================================
# Mesmos comandos do controle pelo
# teclado, agora no controle do Xbox.
#
# Joystick ESQUERDO = anda e gira
# Joystick DIREITO  = levanta e
#                     abaixa a haste
# RB / LB           = giram a corda
#
# Nao tem botao de parar: soltou o
# controle, tudo para.
#
# Antes de rodar: controle ligado e
# robo parado.


# ==========================
# SINAL DE INICIO
# ==========================

hub.light.on(Color.RED)

print("CONTROLE XBOX - INICIANDO")


# ==========================
# MOTORES DA TRACAO
# ==========================

motor_esquerdo = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motor_direito = Motor(Port.B)


# ==========================
# MOTOR DA HASTE - PORTA C
# ==========================
# Positivo = LEVANTAR.

motor_haste = Motor(Port.C, Direction.CLOCKWISE)


# ==========================
# MOTOR DA CORDA - PORTA D
# ==========================

motor_corda = Motor(Port.D, Direction.CLOCKWISE)


# ==========================
# MEDIDAS DO ROBO
# ==========================
# Em MILIMETROS

DIAMETRO_RODA = 55        # mm
DISTANCIA_RODAS = 143     # mm


# ==========================
# VELOCIDADES
# ==========================
# Tracao: velocidade com o joystick
# empurrado ate o fim. Empurrar
# menos anda mais devagar.
#
# Iguais as do teclado: la cada roda
# girava a 100 graus/s, o que da
# ~48 mm/s reto e ~38 graus/s no
# giro.

VELOCIDADE_RETA = 48            # mm por segundo
VELOCIDADE_GIRO = 38            # graus por segundo

# Haste: tambem e o maximo, com o
# joystick direito ate o fim.

VELOCIDADE_HASTE_SUBIDA = 90    # graus por segundo
VELOCIDADE_HASTE_DESCIDA = 180  # graus por segundo

VELOCIDADE_CORDA = 900          # graus por segundo


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


# ==========================
# CONECTAR O CONTROLE
# ==========================
# Primeira vez com este hub: segure
# o botao de parear (atras do
# controle) ate o botao Xbox piscar
# rapido, e so entao rode o programa.

print("Procurando o controle...")

controle = XboxController()

print("Controle conectado.")


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
# COMANDOS
# ==========================

print("================================")
print("      CONTROLE DO ROBO")
print("================================")

print("")
print("MOVIMENTACAO - joystick esquerdo:")
print("Cima = FRENTE")
print("Baixo = RE")
print("Esquerda / direita = GIRAR")

print("")
print("HASTE - joystick direito:")
print("Cima = LEVANTAR")
print("Baixo = ABAIXAR")

print("")
print("CORDA:")
print("RB = GIRAR")
print("LB = GIRAR AO CONTRARIO")

print("")
print("Soltou o controle, tudo para.")


# ==========================================================
#                      CONTROLE
# ==========================================================

hub.light.on(Color.GREEN)

while True:

    # ==========================
    # MOVIMENTACAO
    # ==========================
    # Joystick de -100 a 100:
    # cima e direita sao positivos.

    lado, frente = controle.joystick_left()

    robo.drive(
        frente * VELOCIDADE_RETA / 100,
        lado * VELOCIDADE_GIRO / 100
    )


    # ==========================
    # HASTE
    # ==========================
    # So o eixo vertical do joystick
    # direito. Quanto mais empurra,
    # mais rapido.

    _, comando_haste = controle.joystick_right()

    if comando_haste > 0:

        motor_haste.run(comando_haste * VELOCIDADE_HASTE_SUBIDA / 100)

    elif comando_haste < 0:

        motor_haste.run(comando_haste * VELOCIDADE_HASTE_DESCIDA / 100)

    else:

        # Joystick solto
        motor_haste.stop()


    # ==========================
    # CORDA
    # ==========================

    botoes = controle.buttons.pressed()

    if Button.RB in botoes:

        motor_corda.run(VELOCIDADE_CORDA)

    elif Button.LB in botoes:

        motor_corda.run(-VELOCIDADE_CORDA)

    else:

        motor_corda.stop()


    wait(10)
