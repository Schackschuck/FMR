# FMR — robô LEGO SPIKE Prime

Os programas do robô LEGO SPIKE Prime que fez as missões de uma competição de robótica, escritos em [Pybricks](https://pybricks.com) (MicroPython). É um projeto de uso pessoal, deixado aqui documentado.

> [!NOTE]
> LEGO® e SPIKE™ são marcas do Grupo LEGO, que não patrocina nem apoia este projeto.

## Missões

| Missão | Programas | O que faz |
|---|---|---|
| [Missão 2](missao_2/README.md) | `missao2.py` | Pelo controle do Xbox: as setas dirigem, com o giroscópio corrigindo o rumo, e RB e LB abrem e fecham a comporta |
| [Missão 3](missao_3/README.md) | `percurso1.py`, `percurso2.py`, `percurso3.py` | Sozinho: entrega dois canos pesados, em três programas rodados um depois do outro |
| [Missão 4](missao_4/README.md) | `missao4.py`, `missao4_gravacao.py` | Pelo controle do Xbox, com a haste e a corda. A versão de gravação imprime cada movimento como código, para montar a versão autônoma |

Em `testes/`:

| Programa | O que faz |
|---|---|
| `teste_rapido.py` | Anda 10 cm e abre a garra, para conferir as medidas e o sentido dos motores |
| `teste_garra.py` | Mexe só a garra: três ciclos sozinha e depois pelas setas do hub |
| `controle_xbox.py` | Controle remoto pelo Xbox, com os mesmos comandos da missão 4 |

## Rodar no robô

1. Instale o firmware do Pybricks no hub e abra o [Pybricks Code](https://code.pybricks.com) no navegador.
2. Conecte o hub por Bluetooth.
3. Abra o programa e rode. Cada arquivo é independente: nenhum importa outro.
4. Antes, confira o README da missão: em que posição a garra, a comporta ou a haste tem que começar. Nos programas que usam o giroscópio, não mexa no robô até aparecer "Giroscopio pronto." no terminal.

As luzes do hub: vermelho = iniciando, verde = andando ou pronto para dirigir, azul = terminou.

## O robô

| Porta | Peça |
|---|---|
| A | Tração, roda esquerda |
| B | Tração, roda direita |
| C | Haste (missão 4 e `controle_xbox.py`) |
| D | Garra (missão 3 e testes), comporta (missão 2) ou corda (missão 4 e `controle_xbox.py`) |

As rodas têm 55 mm de diâmetro e ficam a 143 mm uma da outra. Velocidades, freio e abertura da garra ficam em constantes maiúsculas no topo de cada programa. Como cada arquivo vai sozinho para o hub, uma medida que muda tem que mudar em todos os arquivos que a declaram.

## Conferir

O Pybricks só roda dentro do hub, então o teste de verdade é no robô. No computador dá para conferir só a sintaxe:

```bash
for f in */*.py; do python3 -c "import ast, sys; ast.parse(open(sys.argv[1], encoding='utf-8').read())" "$f" && echo "$f ok"; done
```

## Desenvolvimento

O projeto é feito com o [Claude Code](https://claude.com/claude-code). As regras dele (o cabeçalho padrão, as portas, o estilo do código e o fluxo do git) estão no [`CLAUDE.md`](CLAUDE.md).

## Licença

[MIT](LICENSE) © 2026 Arthur Schuck
