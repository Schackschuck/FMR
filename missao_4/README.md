# Missão 4 — controle pelo Xbox

Dois programas, com os mesmos comandos:

| Programa | Para quê |
|---|---|
| `missao4.py` | fazer a missão pelo controle |
| `missao4_gravacao.py` | fazer a missão e **gravar**: cada movimento aparece no terminal como linha de código, para montar a versão autônoma |

## Antes de rodar

1. Haste e corda na **posição de largada** da missão. Na gravação isso é
   obrigatório: a posição em que estão ao iniciar vira o zero, e o programa
   autônomo vai ter que começar igual.
2. Controle do Xbox ligado. Na primeira vez com este hub, segure o botão de
   parear (atrás do controle) até o botão Xbox piscar rápido.
3. Rode o programa e espere "Controle conectado." — a luz fica verde.

## Comandos

| Botão | O que faz |
|---|---|
| Seta cima | anda para frente |
| Seta baixo | dá ré |
| Seta esquerda / direita | gira |
| Cima + esquerda/direita | anda fazendo curva |
| Joystick direito, cima | levanta a haste |
| Joystick direito, baixo | abaixa a haste |
| RB | sobe a corda |
| LB | desce a corda (velocidade máxima) |

- Na haste, quanto mais empurra o joystick, mais rápido ela se mexe.
- Soltou o controle, tudo para.

## Gravação (só no `missao4_gravacao.py`)

- Faça a missão inteira com calma, um movimento de cada vez.
- Cada movimento só é impresso uns instantes (0,3 s) **depois de soltar** o
  botão. Toques rápidos no mesmo botão viram um movimento só.
- Ao terminar, copie do terminal as linhas abaixo de
  `# ===== GRAVACAO - MISSAO 4 =====` (`robo.straight`, `robo.turn`,
  `robo.curve`, `motor_haste.run_target`, `motor_corda.run_target`).

## Luzes

Vermelho = iniciando · verde = pronto (e gravando, no `missao4_gravacao.py`)
