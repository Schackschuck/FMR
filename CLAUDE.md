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
| F | Motor da garra |

`motor_a` gira invertido em relação a `motor_b` para o robô andar reto.

## Arquivos

- `spike4.py` — percurso completo com a garra
- `teste_garra.py` — mexe só a garra (automático + manual pelos botões)

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

Luz e bip no início: vermelho = rodando, verde = andando, azul = terminou.
