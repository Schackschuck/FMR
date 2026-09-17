# ==========================
# DIAGNOSTICO DO SPIKE
# ==========================
# Rode ESTE programa quando o robo
# "nao faz nada".
#
# Ele testa uma coisa de cada vez e
# avisa o que esta faltando, sem
# travar em nenhuma etapa.
#
# Deixe o robo com as rodas no ar
# para ele nao sair andando.

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Color, Port
from pybricks.tools import wait


# ==========================
# TESTE 0 - O HUB LIGA?
# ==========================

hub = PrimeHub()

hub.light.on(Color.RED)
hub.speaker.beep(500, 300)

print("==============================")
print("DIAGNOSTICO INICIADO")
print("==============================")
print("Se voce ouviu o bip e a luz")
print("ficou VERMELHA, o programa")
print("esta rodando.")

wait(1000)


# ==========================
# FUNCAO QUE TESTA UMA PORTA
# ==========================

def testar_porta(nome, porta):

    print("------------------------------")
    print("Testando porta", nome)

    try:
        motor = Motor(porta)

    except OSError:
        print("FALHOU: nada ligado em", nome)
        return None

    print("Motor encontrado em", nome)

    print("Girando 1 segundo...")

    motor.run(200)
    wait(1000)
    motor.stop()

    print("Angulo lido:", motor.angle())

    if motor.angle() == 0:
        print("AVISO: o motor nao girou.")
        print("Veja se o cabo esta bem preso.")
    else:
        print("Porta", nome, "OK")

    return motor


# ==========================
# TESTE 1 - MOTORES
# ==========================

motor_a = testar_porta("A", Port.A)
motor_b = testar_porta("B", Port.B)
motor_f = testar_porta("F (garra)", Port.F)


# ==========================
# TESTE 2 - GIROSCOPIO
# ==========================

print("------------------------------")
print("Testando giroscopio")

try:

    hub.imu.reset_heading(0)
    wait(200)

    print("Heading inicial:", hub.imu.heading())
    print("GIRE O ROBO NA MAO agora...")

    for i in range(5):
        wait(1000)
        print("Heading:", hub.imu.heading())

    print("Se o numero mudou, o")
    print("giroscopio esta OK.")

except Exception as erro:

    print("FALHOU no giroscopio:", erro)


# ==========================
# RESULTADO
# ==========================

print("==============================")
print("RESUMO")
print("==============================")
print("Motor A:", "OK" if motor_a else "FALTANDO")
print("Motor B:", "OK" if motor_b else "FALTANDO")
print("Garra F:", "OK" if motor_f else "FALTANDO")

hub.light.on(Color.BLUE)
hub.speaker.beep(800, 300)

print("DIAGNOSTICO TERMINADO")
