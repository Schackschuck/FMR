# Missão 4 — controle pelo Xbox com gravação

Programa: `missao4.py`

Você dirige o robô pelo controle e cada movimento aparece no terminal como
linha de código. Essas linhas servem para montar a versão autônoma da missão.

## Antes de rodar

1. Haste e corda na **posição de largada** da missão: a posição em que estão
   ao iniciar vira o zero, e o programa autônomo vai ter que começar igual.
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
| RB | gira a corda |
| LB | gira a corda ao contrário |

- Na haste, quanto mais empurra o joystick, mais rápido ela se mexe.
- Soltou o controle, tudo para.

## Gravação

- Faça a missão inteira com calma, um movimento de cada vez.
- Cada movimento só é impresso uns instantes (0,3 s) **depois de soltar** o
  botão. Toques rápidos no mesmo botão viram um movimento só.
- Ao terminar, copie do terminal as linhas abaixo de
  `# ===== GRAVACAO - MISSAO 4 =====` (`robo.straight`, `robo.turn`,
  `robo.curve`, `motor_haste.run_target`, `motor_corda.run_target`).

## Luzes

Vermelho = iniciando · verde = gravando
