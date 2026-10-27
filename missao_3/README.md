# Missão 3 — entrega dos dois canos

São três programas, rodados **um depois do outro**, sem mover o robô de
lugar entre eles.

| Ordem | Programa | Garra |
|---|---|---|
| 1º | `percurso1.py` | vazia |
| 2º | `percurso2.py` | primeiro cano |
| 3º | `percurso3.py` | segundo cano |

## Passo a passo

1. Garra **fechada** e vazia. Rode o `percurso1.py`.
2. Quando a luz ficar azul: coloque o **primeiro cano** e feche a garra nele
   **na mão**. Rode o `percurso2.py`.
3. Quando a luz ficar azul: coloque o **segundo cano** e feche a garra nele
   **na mão**. Rode o `percurso3.py`.

Em todos: depois de iniciar, **não mexa no robô** até aparecer
"Giroscopio pronto." no terminal.

## Luzes

Vermelho = iniciando · verde = andando · azul = terminou

## Se o robô empinar com o cano

Diminua `DESACELERACAO_RETA` no `percurso2.py` / `percurso3.py` (freio mais
suave). Não adianta mexer na velocidade.
