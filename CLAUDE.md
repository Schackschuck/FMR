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
- `teste_garra.py` — testa só a garra (automático + manual pelos botões)
- `diagnostico.py` — testa portas A, B, F e o giroscópio, um de cada vez

## Estilo do código

- Comentários e mensagens em português, sem acento nos `print`
- Banners de comentário `# =====` separando cada bloco
- Linhas em branco generosas entre blocos
- Nomes de função e variável em português (`andar`, `girar_esquerda`,
  `fechar_garra`, `VELOCIDADE_GIRO`)
- Valores de ajuste ficam em constantes MAIÚSCULAS no topo, não espalhados
  pelo código

## Cuidados que já custaram tempo

- Todo movimento de garra tem tempo limite. `run_until_stalled` pode prender o
  programa para sempre se a garra girar livre.
- Motor que pode não estar conectado vai dentro de `try/except OSError` — senão
  o programa inteiro morre na criação do objeto, antes de qualquer `print`.
- Luz e bip no início: vermelho = rodando, verde = andando, azul = terminou.
  Serve para separar "erro no código" de "programa nem iniciou".
