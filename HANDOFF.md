# Handoff — FMR / Spike 4 (Pybricks) — 2026-09-18 18:30

Branch: `claude/spike4-pybricks-3u6336` · Último commit: `28ee77f Divide o percurso em dois programas e alivia o freio com carga`

## 1. Objetivo

Programar um robô LEGO SPIKE Prime em Pybricks (MicroPython) para executar um
percurso fixo de 26 passos, transportando um **cano pesado** numa garra
motorizada. O robô anda distâncias medidas em centímetros, faz curvas de 90° e
180° usando o giroscópio do hub, e abre a garra em dois pontos do percurso.

O percurso roda em **três programas separados**, porque um cano é colocado na
garra antes de cada uma das duas entregas (ver seção 4).

O usuário é quem roda os programas no robô físico — nenhum código deste
repositório roda no ambiente de desenvolvimento, porque `pybricks` só existe
dentro do hub. Todo teste é manual, no robô.

O repositório não tem build, dependências nem testes automatizados. São cinco
programas Python independentes, cada um colado/baixado no hub pelo Pybricks
Code.

## 2. Estado atual

**Confirmado funcionando no robô pelo usuário:**

- Tração andando reto com `DriveBase` + `use_gyro(True)`
- Motor da garra na porta D, abrindo e fechando
- O percurso rodou o suficiente para o usuário observar o robô **empinando para
  frente** ao parar com o cano na garra — foi esse relato que motivou a divisão
  em dois programas e o freio suave

**Escrito e revisado, mas NÃO testado no robô:**

- `percurso1.py`, `percurso2.py` e `percurso3.py` — a divisão em três programas
  é recente, assim como a velocidade de 350 mm/s e a garra em 50°
- A metade de velocidade e o freio suave do `percurso2.py`
  (`straight_acceleration=(250, 60)`) — os valores 250 e 60 são um ponto de
  partida, não medidos
- `Direction.CLOCKWISE` na garra, depois de uma mudança na estrutura do robô
- `DISTANCIA_RODAS = 143` mm — medido e informado pelo usuário, mas nenhuma
  curva foi executada depois disso
- `DIAMETRO_RODA = 55` mm nunca foi validado com régua (seção 5, item 2)


## 3. Arquivos e trechos relevantes

- **`CLAUDE.md`** — regras fixas do projeto, escritas a pedido do usuário ao
  longo das sessões: cabeçalho padrão obrigatório, mapa de portas, proibição de
  teste de porta, proibição de bipe, convenções da garra, estilo do código e a
  configuração de velocidade/freio com carga. **Ler antes de tocar em qualquer
  `.py`.** Essas regras vieram de correções explícitas do usuário, não de
  preferência do assistente.

- **`percurso1.py`** (224 linhas) — passos 1 a 7, robô **vazio**, velocidade
  normal (200 mm/s, 100 graus/s). Não declara o motor da garra, porque não usa.
  Termina no ponto onde o cano é colocado na garra e imprime isso no console.

- **`percurso2.py`** — passos 9 a 16: retão de 88 cm, leva o primeiro cano,
  solta e volta.
  **`percurso3.py`** — passos 17 a 26: gira 180°, leva o segundo cano, solta e
  volta. Os dois têm a mesma configuração; só o trecho do percurso difere.
  - Linhas 68–72: velocidades pela metade (100 mm/s, 50 graus/s)
  - Linhas 82–89: `ACELERACAO_RETA`/`DESACELERACAO_RETA` e os equivalentes de
    giro — é aqui que se ajusta a empinada
  - Linhas 113–126: `robo.settings()` com as tuplas `(acelerar, desacelerar)`
  - Passo 13 e passo 22: as duas aberturas da garra

- **`teste_rapido.py`** (150 linhas) — anda 10 cm e abre a garra. Programa para
  validar medidas e sentido antes de rodar o percurso. Imprime o desvio do rumo
  e o ângulo da garra.

- **`teste_garra.py`** (140 linhas) — não anda. Faz 3 ciclos abre/fecha
  automáticos e depois entra em modo manual pelas setas do hub (esquerda fecha,
  direita abre).

## 4. Decisões tomadas e o porquê

**Percurso dividido em três programas, cortando depois dos passos 7 e 16.** Os
cortes foram pedidos pelo usuário e caem nos pontos onde um cano é colocado na
garra. Programas separados são mais simples do que um só com pausas longas
esperando o operador, e permitem repetir uma das partes sem rodar as outras.
Dois efeitos colaterais: o giroscópio é zerado no início de cada programa, então
as curvas são relativas a onde ele começa (não mover o robô entre os programas);
e o ângulo da garra também é zerado, o que resolveu o problema antigo de a garra
abrir duas vezes sem fechar — hoje cada programa abre uma vez, a partir da garra
fechada na mão.

**Acelera normal, freia devagar — não velocidade baixa em tudo.** O robô
empinava ao **parar**, não ao andar: é a frenagem que joga o peso do cano para
frente. Em Pybricks, `straight_acceleration` e `turn_acceleration` aceitam uma
tupla `(aceleração, desaceleração)`, então o `percurso2.py` usa
`(250, 60)` e `(300, 100)` — arrancada normal, freio manso. A metade da
velocidade (pedida pelo usuário) soma-se a isso. Se voltar a empinar, **baixar
o segundo valor da tupla** é o ajuste certo, não a velocidade.

**Tração por `DriveBase` com `use_gyro(True)`, nunca motor por motor.** A
primeira versão mandava os dois motores com valores espelhados e esperava que
fossem juntos — qualquer diferença de atrito tortava o robô e nada corrigia. O
`DriveBase` iguala as rodas e o giroscópio corrige o rumo durante o trajeto. As
curvas são `robo.turn()`, que também usa o giroscópio. Voltar atrás custa
reescrever `andar`, `re` e os dois `girar_*` nos dois programas.

**Sentido de rotação corrigido na criação do motor, nunca no sinal da chamada.**
`Motor(Port.D, Direction.CLOCKWISE)`. Trocar o sinal dentro de `abrir_garra()`
faria `ABERTURA_GARRA` positivo significar "fechar" e confundiria toda leitura
futura. Com o ajuste na criação do motor, positivo é sempre abrir, e uma mudança
de estrutura do robô é **uma linha** por arquivo.

**Nada de verificação de porta ou de travamento — decisão explícita do usuário.**
Uma versão anterior tinha `try/except OSError` em volta de `Motor(...)`,
`run_until_stalled` com `duty_limit` e detecção de travamento por `speed()`. O
usuário mandou tirar tudo: "só mande o motor mexer". **Não reintroduzir** —
está proibido no `CLAUDE.md`.

**Constantes repetidas em cada arquivo, de propósito.** Cada programa é baixado
sozinho no hub, então precisa ser autossuficiente. O custo é real (seção 6).

**Sem bipe.** `hub.speaker.beep()` foi removido a pedido do usuário. Só luz:
vermelho = rodando, verde = andando, azul = terminou.

**Medidas em milímetros.** O `DriveBase` usa mm, então as constantes do robô são
mm (`DIAMETRO_RODA = 55`), mas `andar()` e `re()` recebem **centímetros** e
multiplicam por 10 internamente — as chamadas do percurso ficam legíveis
(`andar(210)` = 2,10 m).

## 5. Pendências e próximos passos

1. **Rodar os três programas em sequência no robô.** Nenhum deles foi testado
   depois da divisão, da subida para 350 mm/s e da garra em 50°.
2. **Rodar `teste_rapido.py` e medir com régua quanto o robô andou.** Se andou
   diferente de 10 cm, ajustar `DIAMETRO_RODA` proporcionalmente
   (`55 × pedido/medido`) em **todos** os arquivos que o declaram.
3. **Rodar `percurso2.py` com o cano e ver se ainda empina.** Se empinar,
   baixar `DESACELERACAO_RETA` (hoje 60) para 40 ou 30, nos dois programas que
   carregam cano. A 350 mm/s com freio de 60 mm/s², a frenagem começa com quase
   um metro de antecedência — se ficar lento demais, subir a desaceleração antes
   de mexer na velocidade.
4. **Confirmar que a garra abre para o lado certo** com o `Direction.CLOCKWISE`
   novo, depois da mudança de estrutura.
5. **Conferir se as curvas de 90° e o giro de 180° fecham o ângulo** com
   `DISTANCIA_RODAS = 143`.
6. **Abrir PR, se o usuário pedir.** Nenhum PR foi aberto — o trabalho só foi
   commitado e enviado para a branch.

## 6. Problemas conhecidos e armadilhas

- **A garra tem que estar FECHADA no cano antes de rodar o `percurso2.py` e o
  `percurso3.py`.** `motor_garra.reset_angle(0)` define a posição atual como
  zero; o operador fecha a garra na mão entre os programas.
- **O robô tem que estar PARADO no início de cada programa.** Os dois esperam
  `hub.imu.ready()`; mexer no robô nesse intervalo estraga a calibração do
  giroscópio e a linha reta sai torta.
- **Não mover o robô entre um programa e o próximo.** Cada um zera o rumo onde
  começa; girar o robô na mão ao colocar o cano desloca todas as curvas
  seguintes.
- **Constantes duplicadas em cinco arquivos.** `DIAMETRO_RODA` e
  `DISTANCIA_RODAS` estão em `percurso1.py`, `percurso2.py`, `percurso3.py` e
  `teste_rapido.py`; `ABERTURA_GARRA` e a `Direction` da garra estão em
  `percurso2.py`, `percurso3.py`, `teste_garra.py` e `teste_rapido.py`. Mudar em
  um só deixa o projeto inconsistente — **sempre mudar em todos**. Um módulo
  compartilhado resolveria, mas não foi verificado se o Pybricks Code do usuário suporta
  múltiplos arquivos no hub.
- **`robo.turn()` negativo gira para a ESQUERDA**, positivo para a direita. É
  contraintuitivo; `girar_esquerda()` existe para esconder esse sinal.
- **Qual motor é o esquerdo foi deduzido, não confirmado.** `Port.A` é tratado
  como esquerdo (com `Direction.COUNTERCLOCKWISE`), inferido pelos sinais do
  código original do usuário. Se o robô girar para o lado errado, trocar A e B
  na criação do `DriveBase`.
- **Não existe forma de testar lógica aqui.** `pybricks` não está instalado e
  não pode ser. O único check disponível é de sintaxe (seção 7). Qualquer
  afirmação de "funciona" tem que vir de uma rodada no robô, feita pelo usuário.
- **Tentativa que já falhou e não vale repetir:** proteger a garra com
  `try/except OSError` e detectar travamento. Foi implementado, o usuário mandou
  remover, e hoje está proibido no `CLAUDE.md`.

## 7. Como rodar e testar

**No robô (é o único teste que vale):**

1. Abrir o Pybricks Code em <https://code.pybricks.com>
2. Conectar o hub SPIKE Prime por Bluetooth
3. Colar o conteúdo do programa desejado e rodar
4. Deixar a garra **fechada** e o robô **parado** antes de dar start

Ordem do percurso completo:

1. `percurso1.py` — robô vazio, termina pedindo o cano
2. Colocar o primeiro cano e fechar a garra nele, **sem mover o robô de lugar**
3. `percurso2.py` — entrega o primeiro cano e volta
4. Colocar o segundo cano e fechar a garra nele, sem mover o robô
5. `percurso3.py` — gira 180°, entrega o segundo cano e volta

Para calibrar antes: `teste_garra.py` (só a garra) e `teste_rapido.py` (10 cm).

Portas: A = tração esquerda, B = tração direita, D = garra.

Luz do hub: vermelha no início, verde durante o percurso, azul no fim. Se a luz
não acender, o programa não iniciou — o problema não está no código.

**No repositório (só sintaxe):**

```bash
cd /home/user/FMR
for f in percurso1.py percurso2.py percurso3.py teste_garra.py teste_rapido.py; do
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
