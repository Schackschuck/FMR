# FMR — Spike 4 (Pybricks)

Projeto de robótica LEGO SPIKE Prime programado em Pybricks (MicroPython).

## Regra fixa: cabeçalho padrão

**Todo arquivo `.py` deste projeto começa exatamente com este bloco**, antes de
qualquer comentário, banner ou código:

```python
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
```

Vale mesmo que o programa não use todos os imports — o bloco é sempre o mesmo,
completo, sem cortar linha. Não reordenar, não enxugar, não trocar por imports
parciais.

## Portas

| Porta | Peça |
|---|---|
| A | Motor de tração (esquerda) |
| B | Motor de tração (direita) |
| D | Motor da garra |

O motor esquerdo é criado com `Direction.COUNTERCLOCKWISE`, para que valor
positivo signifique "para frente" nos dois — é o que o `DriveBase` espera.

## Tração: sempre DriveBase com giroscópio

Nada de controlar `motor_esquerdo` e `motor_direito` separados para andar.
A tração é sempre:

```python
robo = DriveBase(motor_esquerdo, motor_direito,
                 wheel_diameter=DIAMETRO_RODA, axle_track=DISTANCIA_RODAS)
robo.use_gyro(True)
```

- `robo.straight(mm)` anda reto; negativo dá ré
- `robo.turn(graus)` gira; **negativo = esquerda**, positivo = direita
- Medidas do robô em **milímetros** (o `DriveBase` usa mm)
- Antes de andar, esperar `hub.imu.ready()` com o robô parado

## Arquivos

- `spike4.py` — percurso completo com a garra
- `teste_garra.py` — mexe só a garra (automático + manual pelos botões)
- `teste_rapido.py` — anda 10 cm e abre a garra, para conferir medidas

## Estilo do código

- Comentários e mensagens em português, sem acento nos `print`
- Banners de comentário `# =====` separando cada bloco
- Linhas em branco generosas entre blocos
- Nomes de função e variável em português (`andar`, `girar_esquerda`,
  `fechar_garra`, `VELOCIDADE_GIRO`)
- Valores de ajuste ficam em constantes MAIÚSCULAS no topo, não espalhados
  pelo código

## Regra fixa: nada de teste de porta

Não verificar se o motor está presente na porta, não usar `try/except OSError`
em volta de `Motor(...)`, não detectar travamento com `run_until_stalled` nem
com leitura de `speed()`. O motor recebe o comando e gira — só isso.

A garra abre e fecha com `run_angle` em `ABERTURA_GARRA` graus, positivo para
abrir e negativo para fechar.

## Sinal visual

Só luz, **sem bipe**: vermelho = rodando, verde = andando, azul = terminou.
Não usar `hub.speaker.beep()`.

## Garra

O motor da garra é criado com `Direction.COUNTERCLOCKWISE`, porque o sentido
está invertido no robô. Com isso, `run_angle` positivo continua sendo **abrir**
e negativo **fechar**.

Logo depois de criar o motor vem `motor_garra.reset_angle(0)`: a posição em que
a garra está ao iniciar o programa passa a valer como ângulo zero. Por isso a
garra deve estar **fechada** antes de rodar qualquer programa.

`ABERTURA_GARRA = 35` graus.
