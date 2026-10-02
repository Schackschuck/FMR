from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

from pybricks.iodevices import XboxController


# ==========================================================
#             MISSAO 4 - XBOX COM GRAVACAO
# ==========================================================
# Mesmos comandos do controle pelo
# teclado, agora no controle do Xbox.
#
# Direcional (setas) = anda e gira
# Joystick DIREITO   = levanta e
#                      abaixa a haste
# RB / LB            = giram a corda
#
# Cada movimento feito sai no terminal
# como linha de codigo, para copiar e
# montar a versao autonoma da missao.
#
# Nao tem botao de parar: soltou o
# controle, tudo para.
#
# Antes de rodar: controle ligado.


# ==========================
# SINAL DE INICIO
# ==========================

hub.light.on(Color.RED)

print("MISSAO 4 - INICIANDO")


# ==========================
# MOTORES DA TRACAO
# ==========================

motor_esquerdo = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motor_direito = Motor(Port.B)


# ==========================
# MOTOR DA HASTE - PORTA C
# ==========================
# Positivo = LEVANTAR.
#
# A posicao em que a haste esta ao
# ligar o programa vira o zero. O
# programa autonomo tem que comecar
# com a haste na mesma posicao.

motor_haste = Motor(Port.C, Direction.CLOCKWISE)
motor_haste.reset_angle(0)


# ==========================
# MOTOR DA CORDA - PORTA D
# ==========================
# A posicao em que a corda esta ao
# ligar o programa vira o zero. O
# programa autonomo tem que comecar
# com a corda na mesma posicao.

motor_corda = Motor(Port.D, Direction.CLOCKWISE)
motor_corda.reset_angle(0)


# ==========================
# MEDIDAS DO ROBO
# ==========================
# Em MILIMETROS

DIAMETRO_RODA = 55        # mm
DISTANCIA_RODAS = 143     # mm


# ==========================
# VELOCIDADES
# ==========================
# Tracao: o direcional nao tem meio
# termo, entao anda sempre nessas
# velocidades.
#
# Iguais as do teclado: la cada roda
# girava a 100 graus/s, o que da
# ~48 mm/s reto e ~38 graus/s no
# giro.

VELOCIDADE_RETA = 48            # mm por segundo
VELOCIDADE_GIRO = 38            # graus por segundo

# Haste: e o maximo, com o joystick
# direito ate o fim.

VELOCIDADE_HASTE_SUBIDA = 90    # graus por segundo
VELOCIDADE_HASTE_DESCIDA = 180  # graus por segundo

VELOCIDADE_CORDA = 900          # graus por segundo


# ==========================
# GRAVACAO
# ==========================
# Um movimento so termina depois de
# solto por este tempo: assim entra
# o que o robo ainda rolou, e toques
# rapidos no mesmo botao viram um
# movimento so.

TEMPO_ASSENTAR = 300            # ms

# Para converter o giro em radianos
# no calculo do raio da curva.

GRAUS_POR_RADIANO = 57.2958


# ==========================
# O ROBO
# ==========================

robo = DriveBase(
    motor_esquerdo,
    motor_direito,
    wheel_diameter=DIAMETRO_RODA,
    axle_track=DISTANCIA_RODAS
)

# SEM giroscopio, de proposito: aqui
# quem corrige o rumo e quem dirige.
# Com ele, os movimentos curtos davam
# trancos e o robo tremia parado.

robo.use_gyro(False)


# ==========================
# FUNCOES DE GRAVACAO
# ==========================
# Cada mecanismo (tracao, haste,
# corda) tem um "trecho":
#
# comando  = o que esta sendo feito
#            (None = nada aberto).
#            Tracao: (velocidade, giro).
#            Haste e corda: 1 ou -1.
# inicio   = ms em que o trecho abriu
# soltou_em = ms em que foi solto
#            (None = ainda apertado)
# partida  = leitura dos sensores
#            quando o trecho abriu

def novo_trecho():

    return {"comando": None, "inicio": 0, "soltou_em": None, "partida": None}


def ler_tracao():

    return (robo.distance(), robo.angle())


def ler_haste():

    return motor_haste.angle()


def ler_corda():

    return motor_corda.angle()


def atualizar_trecho(trecho, comando, agora, ler, fechar):

    # comando = None quando nada esta apertado para esse mecanismo

    if comando is not None:

        trecho["soltou_em"] = None

        if trecho["comando"] == comando:
            return

        if trecho["comando"] is not None:
            fechar(trecho, ler())

        trecho["comando"] = comando
        trecho["inicio"] = agora
        trecho["partida"] = ler()

    elif trecho["comando"] is not None:

        if trecho["soltou_em"] is None:
            trecho["soltou_em"] = agora

        elif agora - trecho["soltou_em"] >= TEMPO_ASSENTAR:
            fechar(trecho, ler())
            trecho["comando"] = None
            trecho["soltou_em"] = None


def fechar_tracao(trecho, final):

    distancia = final[0] - trecho["partida"][0]
    angulo = final[1] - trecho["partida"][1]

    velocidade, giro = trecho["comando"]
    t = trecho["inicio"] / 1000

    # Nao andou: nao imprime nada
    if abs(distancia) < 1 and abs(angulo) < 1:
        return

    if giro == 0:

        print("robo.straight({})  # t={:.1f}s".format(int(round(distancia)), t))

    elif velocidade == 0:

        print("robo.turn({})  # t={:.1f}s".format(int(round(angulo)), t))

    elif abs(angulo) < 1:

        # Curva que nao girou: conta como reto
        print("robo.straight({})  # t={:.1f}s".format(int(round(distancia)), t))

    else:

        # Com este raio, a curva refaz exatamente
        # a distancia e o giro medidos.
        raio = distancia * GRAUS_POR_RADIANO / abs(angulo)

        print("robo.curve({}, {})  # t={:.1f}s, andou {} mm, girou {} graus".format(
            int(round(raio)), int(round(angulo)), t,
            int(round(distancia)), int(round(angulo))))


def fechar_haste(trecho, final):

    if trecho["comando"] == 1:
        velocidade = VELOCIDADE_HASTE_SUBIDA
    else:
        velocidade = VELOCIDADE_HASTE_DESCIDA

    variacao = final - trecho["partida"]
    t = trecho["inicio"] / 1000

    if abs(variacao) < 1:
        return

    print("motor_haste.run_target({}, {})  # t={:.1f}s, {:+d} graus".format(
        velocidade, int(round(final)), t, int(round(variacao))))


def fechar_corda(trecho, final):

    variacao = final - trecho["partida"]
    t = trecho["inicio"] / 1000

    if abs(variacao) < 1:
        return

    print("motor_corda.run_target({}, {})  # t={:.1f}s, {:+d} graus".format(
        VELOCIDADE_CORDA, int(round(final)), t, int(round(variacao))))


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
print("      CONTROLE DO ROBO")
print("================================")

print("")
print("MOVIMENTACAO - direcional (setas):")
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

print("")
print("Cada movimento aparece abaixo como")
print("linha de codigo, ao terminar.")


# ==========================
# INICIO DA GRAVACAO
# ==========================

trecho_tracao = novo_trecho()
trecho_haste = novo_trecho()
trecho_corda = novo_trecho()

cronometro = StopWatch()

print("")
print("# ===== GRAVACAO - MISSAO 4 =====")


# ==========================================================
#                      CONTROLE
# ==========================================================

hub.light.on(Color.GREEN)

while True:

    # ==========================
    # LER OS BOTOES
    # ==========================

    botoes = controle.buttons.pressed()
    agora = cronometro.time()


    # ==========================
    # MOVIMENTACAO
    # ==========================
    # Direcional (setas). Da para
    # apertar duas juntas: cima com
    # direita anda fazendo curva.

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

    if velocidade == 0 and giro == 0:

        # Nenhuma seta: motores soltos.
        # drive(0, 0) deixaria os motores
        # segurando o robo, com barulho.
        robo.stop()

        comando_tracao = None

    else:

        robo.drive(velocidade, giro)

        comando_tracao = (velocidade, giro)

    atualizar_trecho(trecho_tracao, comando_tracao, agora, ler_tracao, fechar_tracao)


    # ==========================
    # HASTE
    # ==========================
    # So o eixo vertical do joystick
    # direito. Quanto mais empurra,
    # mais rapido.

    _, comando_haste = controle.joystick_right()

    if comando_haste > 0:

        motor_haste.run(comando_haste * VELOCIDADE_HASTE_SUBIDA / 100)

        sentido_haste = 1

    elif comando_haste < 0:

        motor_haste.run(comando_haste * VELOCIDADE_HASTE_DESCIDA / 100)

        sentido_haste = -1

    else:

        # Joystick solto
        motor_haste.stop()

        sentido_haste = None

    atualizar_trecho(trecho_haste, sentido_haste, agora, ler_haste, fechar_haste)


    # ==========================
    # CORDA
    # ==========================

    if Button.RB in botoes:

        motor_corda.run(VELOCIDADE_CORDA)

        sentido_corda = 1

    elif Button.LB in botoes:

        motor_corda.run(-VELOCIDADE_CORDA)

        sentido_corda = -1

    else:

        motor_corda.stop()

        sentido_corda = None

    atualizar_trecho(trecho_corda, sentido_corda, agora, ler_corda, fechar_corda)


    wait(10)
