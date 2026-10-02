from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

from pybricks.iodevices import XboxController


# ==========================================================
#          MISSAO 2 - CONTROLE PELO XBOX
# ==========================================================
# O robo e dirigido pelo controle do
# Xbox. Tracao: motores A e B.
# Comporta: motor D.
#
# Setas = velocidade fixa, com o
#         giroscopio corrigindo os
#         desvios no meio do caminho.
#
# RB    = abre a comporta
# LB    = fecha a comporta
#
# Soltou as setas, o robo para.
#
# Antes de rodar: controle ligado e
# comporta FECHADA.


# ==========================
# SINAL DE INICIO
# ==========================

hub.light.on(Color.RED)

print("MISSAO 2 - INICIANDO")


# ==========================
# MOTORES DA TRACAO
# ==========================

motor_esquerdo = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motor_direito = Motor(Port.B)


# ==========================
# MOTOR DA COMPORTA - PORTA D
# ==========================
# Positivo = ABRIR, negativo = FECHAR.
# O sentido se ajusta aqui, na criacao
# do motor: se abrir para o lado
# errado, troque a Direction.

motor_comporta = Motor(Port.D, Direction.CLOCKWISE)

# A posicao em que a comporta esta ao
# iniciar passa a valer como zero.
# Por isso ela deve estar FECHADA
# antes de rodar.

motor_comporta.reset_angle(0)


# ==========================
# MEDIDAS DO ROBO
# ==========================
# Em MILIMETROS

DIAMETRO_RODA = 55        # mm
DISTANCIA_RODAS = 143     # mm


# ==========================
# VELOCIDADES
# ==========================
# As setas andam sempre nessas
# velocidades.

VELOCIDADE_RETA = 200     # mm por segundo
VELOCIDADE_GIRO = 100     # graus por segundo


# ==========================
# COMPORTA
# ==========================
# Abrir e fechar giram essas voltas.
# A comporta vai ate a POSICAO (fechada
# = 0, aberta = voltas), nao "mais
# N voltas": apertar duas vezes o
# mesmo botao nao passa do fim.

VOLTAS_COMPORTA = 6
VELOCIDADE_COMPORTA = 720                  # graus por segundo

COMPORTA_FECHADA = 0                       # graus
COMPORTA_ABERTA = VOLTAS_COMPORTA * 360    # graus


# ==========================
# O ROBO
# ==========================

robo = DriveBase(
    motor_esquerdo,
    motor_direito,
    wheel_diameter=DIAMETRO_RODA,
    axle_track=DISTANCIA_RODAS
)

# COM giroscopio, de proposito: nesta
# missao ele corrige os desvios no
# meio do caminho. Parado, o robo
# fica solto (brake), para nao tremer
# nem dar tranco.

robo.use_gyro(True)

# O giroscopio so calibra com o robo
# PARADO: nao mexa nele ate liberar.

print("Calibrando o giroscopio...")

while not hub.imu.ready():

    wait(10)

print("Giroscopio pronto.")


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
# COMANDOS
# ==========================

print("================================")
print("        MISSAO 2 - XBOX")
print("================================")

print("")
print("SETAS - velocidade fixa:")
print("Cima = FRENTE")
print("Baixo = RE")
print("Esquerda / direita = GIRAR")

print("")
print("O giroscopio corrige o rumo.")

print("")
print("COMPORTA:")
print("RB = ABRIR")
print("LB = FECHAR")

print("")
print("Soltou as setas, o robo para.")


# ==========================================================
#                      CONTROLE
# ==========================================================

hub.light.on(Color.GREEN)

# A comporta comeca FECHADA.

alvo_comporta = COMPORTA_FECHADA

while True:

    # ==========================
    # SETAS
    # ==========================
    # Da para apertar duas juntas:
    # cima com direita anda fazendo
    # curva.

    botoes = controle.buttons.pressed()

    velocidade = 0
    giro = 0

    if Button.UP in botoes:

        velocidade = VELOCIDADE_RETA

    elif Button.DOWN in botoes:

        velocidade = -VELOCIDADE_RETA

    if Button.RIGHT in botoes:

        giro = VELOCIDADE_GIRO

    elif Button.LEFT in botoes:

        giro = -VELOCIDADE_GIRO


    # ==========================
    # ANDAR OU PARAR
    # ==========================

    if velocidade == 0 and giro == 0:

        # Nada apertado: freia as rodas
        # sem ficar segurando o robo, entao
        # nao tem barulho nem tranco. Nao
        # usar drive(0, 0): com o giroscopio
        # ele segura o robo o tempo todo.
        robo.brake()

    else:

        robo.drive(velocidade, giro)


    # ==========================
    # COMPORTA
    # ==========================
    # RB abre, LB fecha. Os dois juntos
    # nao fazem nada. Sem esperar o
    # fim: o robo continua obedecendo
    # as setas enquanto ela se mexe.

    abrir = Button.RB in botoes and Button.LB not in botoes
    fechar = Button.LB in botoes and Button.RB not in botoes

    if abrir and alvo_comporta != COMPORTA_ABERTA:

        alvo_comporta = COMPORTA_ABERTA

        motor_comporta.run_target(VELOCIDADE_COMPORTA, alvo_comporta, wait=False)

    elif fechar and alvo_comporta != COMPORTA_FECHADA:

        alvo_comporta = COMPORTA_FECHADA

        motor_comporta.run_target(VELOCIDADE_COMPORTA, alvo_comporta, wait=False)


    wait(10)
