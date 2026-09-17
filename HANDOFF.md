# Handoff — FMR / Spike 4 (Pybricks) — 2026-09-17 21:42

Branch: `claude/spike4-pybricks-3u6336` · Último commit: `ab95723 Inverte a rotacao da garra apos mudanca na estrutura`

## 1. Objetivo

Programar um robô LEGO SPIKE Prime em Pybricks (MicroPython) para executar um
percurso fixo de 17 passos com uma garra motorizada. O robô anda distâncias
medidas em centímetros, faz curvas de 90° usando o giroscópio do hub e abre a
garra em um ponto específico do percurso.

O usuário é quem roda os programas no robô físico — nenhum código deste
repositório roda no ambiente de desenvolvimento, porque `pybricks` só existe
dentro do hub. Todo teste é manual, no robô.

O repositório não tem build, dependências nem testes automatizados. São três
programas Python independentes, cada um colado/baixado no hub pelo Pybricks
Code.

## 2. Estado atual

**Confirmado funcionando no robô pelo usuário:**

- Motor da garra na porta D mexendo, com abertura e sentido corretos na
  estrutura **anterior** do robô
- Tração andando (o usuário validou que a porta D resolveu o problema em que
  "o Spike 4 não fazia nada")

**Escrito e revisado, mas NÃO testado no robô:**

- Percurso de 17 passos em `spike4.py` (escrito nesta sessão, nunca rodado)
- `Direction.CLOCKWISE` na garra — o usuário mudou a estrutura do robô e pediu
  a inversão; ninguém rodou depois da troca
- `ABERTURA_GARRA = 35` graus
- `DISTANCIA_RODAS = 143` mm — valor medido e informado pelo usuário, mas
  nenhuma curva foi executada depois disso
- `DIAMETRO_RODA = 55` mm nunca foi validado com régua (ver seção 5, item 2)

**Não começado:**

- Fechar a garra em algum ponto do percurso (ver seção 6)

## 3. Arquivos e trechos relevantes

- **`CLAUDE.md`** — regras fixas do projeto, escritas a pedido do usuário ao
  longo da sessão: cabeçalho padrão obrigatório, mapa de portas, proibição de
  teste de porta, proibição de bipe, convenções da garra e estilo do código.
  **Ler antes de tocar em qualquer `.py`.** Essas regras vieram de correções
  explícitas do usuário, não de preferência do assistente.

- **`spike4.py`** (397 linhas) — programa principal.
  - Linhas 1–7: cabeçalho padrão obrigatório
  - Linha 40: criação do motor da garra, onde o **sentido** é ajustado
  - Linha 48: `motor_garra.reset_angle(0)`
  - Linhas 58–62: `DIAMETRO_RODA`, `DISTANCIA_RODAS`
  - Linhas 69–71: velocidades
  - Linha 80: `ABERTURA_GARRA = 35`
  - Linhas 91–113: `DriveBase` + `use_gyro(True)` + `settings()`
  - Linhas 123–126: espera `hub.imu.ready()` e zera o rumo
  - Linhas 135–216: funções `andar`, `re`, `girar_esquerda`, `girar_direita`,
    `abrir_garra`, `fechar_garra`, `soltar_garra`
  - Linhas 220–397: o percurso, um bloco comentado por passo (1 a 17)

- **`teste_rapido.py`** (150 linhas) — anda 10 cm e abre a garra. É o programa
  para validar medidas e sentido antes de rodar o percurso inteiro. Imprime o
  desvio do rumo e o ângulo da garra.

- **`teste_garra.py`** (140 linhas) — não anda. Faz 3 ciclos abre/fecha
  automáticos e depois entra em modo manual pelas setas do hub (esquerda fecha,
  direita abre). Serve para achar `ABERTURA_GARRA` no próprio robô.

## 4. Decisões tomadas e o porquê

**Tração por `DriveBase` com `use_gyro(True)`, nunca motor por motor.**
A primeira versão mandava `motor_a` e `motor_b` com valores espelhados e
esperava que fossem juntos — qualquer diferença de atrito tortava o robô e nada
corrigia. O `DriveBase` iguala as rodas, e `use_gyro(True)` faz o robô medir o
próprio desvio e corrigir durante o trajeto. As curvas passaram a ser
`robo.turn()`, que também usa o giroscópio, eliminando o laço manual que lia
`hub.imu.heading()`. Voltar atrás custa reescrever `andar`, `re` e os dois
`girar_*`.

**Sentido de rotação corrigido na criação do motor, nunca no sinal da chamada.**
`Motor(Port.D, Direction.CLOCKWISE)`. Quando a garra girou para o lado errado, a
tentação foi trocar o sinal dentro de `abrir_garra()`, mas isso faria
`ABERTURA_GARRA` positivo significar "fechar" e confundiria toda leitura futura
do código. Com o ajuste na criação do motor, positivo é sempre abrir, e uma
mudança de estrutura do robô é **uma linha** por arquivo.

**Nada de verificação de porta ou de travamento — decisão explícita do usuário.**
Uma versão anterior tinha `try/except OSError` em volta de `Motor(...)`,
`run_until_stalled` com `duty_limit` e detecção de travamento por `speed()`. O
usuário mandou tirar tudo: "só mande o motor mexer". Hoje a garra é
`run_angle(VELOCIDADE_GARRA, ±ABERTURA_GARRA)` e nada mais. **Não reintroduzir
isso**, mesmo parecendo mais seguro — está proibido no `CLAUDE.md`.

**Constantes repetidas em cada arquivo, de propósito.** Cada programa é baixado
sozinho no hub, então precisa ser autossuficiente. O custo é real: mudar uma
medida exige editar mais de um arquivo (ver seção 6).

**Sem bipe.** `hub.speaker.beep()` foi removido a pedido do usuário. Só luz:
vermelho = rodando, verde = andando, azul = terminou.

**Medidas em milímetros.** O `DriveBase` usa mm, então as constantes do robô são
mm (`DIAMETRO_RODA = 55`), mas `andar()` e `re()` recebem **centímetros** e
multiplicam por 10 internamente — as chamadas do percurso ficam legíveis
(`andar(210)` = 2,10 m).

## 5. Pendências e próximos passos

1. **Perguntar ao usuário se falta um `fechar_garra()` no percurso.** O percurso
   atual só **abre** a garra (passo 13, linha 345). Não há nenhum fechamento em
   lugar nenhum. Isso foi sinalizado ao usuário e ele ainda não respondeu. Pode
   ser intencional (a garra começa fechada e solta algo) ou pode ser um passo
   esquecido.
2. **Rodar `teste_rapido.py` e medir com régua quanto o robô andou.** Se andou
   diferente de 10 cm, ajustar `DIAMETRO_RODA` proporcionalmente
   (`55 × pedido/medido`) em `spike4.py:58` **e** `teste_rapido.py:52`.
3. **Confirmar no `teste_rapido.py` que a garra abre para o lado certo** com o
   `Direction.CLOCKWISE` novo, depois da mudança de estrutura. Se estiver
   invertida, trocar para `COUNTERCLOCKWISE` nos três arquivos.
4. **Rodar o percurso completo do `spike4.py`** e conferir se as quatro curvas
   de 90° fecham o ângulo com `DISTANCIA_RODAS = 143`.
5. **Abrir PR, se o usuário pedir.** Nenhum PR foi aberto nesta sessão — o
   trabalho só foi commitado e enviado para a branch.

## 6. Problemas conhecidos e armadilhas

- **A garra tem que estar FECHADA antes do start.** `motor_garra.reset_angle(0)`
  define a posição atual como zero. Iniciar com a garra meio aberta desloca todo
  o curso.
- **O robô tem que estar PARADO no início.** Os programas esperam
  `hub.imu.ready()`; mexer no robô nesse intervalo estraga a calibração do
  giroscópio e a linha reta sai torta.
- **Constantes duplicadas.** `DIAMETRO_RODA` e `DISTANCIA_RODAS` existem em
  `spike4.py` e `teste_rapido.py`; `ABERTURA_GARRA` e a `Direction` da garra
  existem nos três arquivos. Mudar em um só deixa o projeto inconsistente —
  **sempre mudar em todos**. Um módulo compartilhado resolveria, mas não foi
  verificado se o Pybricks Code do usuário suporta múltiplos arquivos no hub.
- **`robo.turn()` negativo gira para a ESQUERDA**, positivo para a direita. É
  contraintuitivo e já causou confusão; `girar_esquerda()` existe justamente
  para esconder esse sinal.
- **Qual motor é o esquerdo foi deduzido, não confirmado.** `Port.A` é tratado
  como esquerdo (com `Direction.COUNTERCLOCKWISE`), inferido pelos sinais do
  código original do usuário. Se o robô girar para o lado errado nas curvas, é
  só trocar A e B na criação do `DriveBase` (`spike4.py:91`).
- **Não existe forma de testar lógica aqui.** `pybricks` não está instalado e não
  pode ser. O único check disponível é de sintaxe (seção 7). Qualquer afirmação
  de "funciona" tem que vir de uma rodada no robô, feita pelo usuário.
- **Tentativa que já falhou e não vale repetir:** proteger a garra com
  `try/except OSError` e detectar travamento. Foi implementado, o usuário mandou
  remover, e hoje está proibido no `CLAUDE.md`.

## 7. Como rodar e testar

**No robô (é o único teste que vale):**

1. Abrir o Pybricks Code em <https://code.pybricks.com>
2. Conectar o hub SPIKE Prime por Bluetooth
3. Colar o conteúdo do programa desejado e rodar
4. Deixar a garra **fechada** e o robô **parado** antes de dar start
5. Ordem recomendada: `teste_garra.py` → `teste_rapido.py` → `spike4.py`

Portas: A = tração esquerda, B = tração direita, D = garra.

O que se espera ver no console do Pybricks ao rodar `spike4.py`:

```
PROGRAMA INICIADO
Preparando giroscopio...
Giroscopio pronto.
PERCURSO INICIADO
1) Andando 2,10 metros...
2) Curva 90 graus esquerda
...
PERCURSO COMPLETO
```

Luz do hub: vermelha no início, verde durante o percurso, azul no fim. Se a luz
não acender, o programa não iniciou — o problema não está no código.

**No repositório (só sintaxe):**

```bash
cd /home/user/FMR
for f in spike4.py teste_garra.py teste_rapido.py; do
  python3 -c "import ast; ast.parse(open('$f').read()); print('$f ok')"
done
```

Isso apenas garante que o arquivo é Python válido. **Não** valida nada de
Pybricks: `import pybricks` falha por design neste ambiente.

**Git:**

```bash
git push -u origin claude/spike4-pybricks-3u6336
```

Sempre nessa branch. Nenhum PR foi aberto — não abrir sem o usuário pedir.
