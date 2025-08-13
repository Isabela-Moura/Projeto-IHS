# **🎮 Fragmentado**

## 👥 Equipe
- **Andreywid Souza** - ayls@cin.ufpe.br
- **Jadiael Gadelha** - jgfl@cin.ufpe.br
- **João Victor Lopes** - jvcl@cin.ufpe.br
- **Mário Daniel** - mdtsf@cin.ufpe.br
- **Victor Diniz** - vpd@cin.ufpe.br

---

## 1. 📖 Visão Geral

### 1.1. Descrição
Fragmentado consiste em um jogo 2D no qual o jogador controla um aluno que perdeu seu crachá no CIn. O objetivo do jogador é encontrar os fragmentos do crachá perdido, recuperar o cartão e passar por uma catraca antes que o tempo acabe e o aluno fique preso no prédio. Ademais, estão espalhados pelo CIn hambúrgueres que, quando consumidos, adicionam tempo no cronômetro e latas de energético que aumentam a velocidade do personagem por um período, auxiliando assim o aluno a alcançar seu objetivo.

---

## 2. 🛠 Arquitetura do Projeto

### 2.1. Estrutura de Diretórios
Duas pastas principais:

- **assets:** pasta contendo todas as imagens e arquivos para sprites e sons do jogo.
- **src:** pasta contendo toda a parte funcional do jogo.

```plaintext
├── assets/
│   ├── gameplay/
│   ├── map/
│   ├── screenshots/
│   ├── tilemap/
├── src/
│   ├── level.py
│   ├── main.py
│   ├── player.py
│   ├── settings.py
│   ├── tile.py
├── README.md
```

### 2.2. Descrição dos Arquivos
- **level.py**: Quase tudo relacionado ao level, coltavéis, etc.
- **main.py**: Ponto de entrada do jogo; class Game que gerencia o loop principal do jogo.
- **player.py**: Classe Player, que gerencia as ações do jogador.
- **settings.py**: Configurações globais do jogo (e.g., tamanho da tela, FPS).
- **assets/**: Contém todos os recursos do jogo, como imagens e sons.

## 3. 📸 Capturas de Tela

### 3.1. Tela Inicial
<img src="/assets/sreenshots/tela-inicial.png">

### 3.2. Gameplay
<img src="/assets/sreenshots/screenshot_59425.png">

### 3.3. Collectibles
<img src="/assets/sreenshots/screenshot_11597.png">

## 4. 🛠 Ferramentas, Bibliotecas e Frameworks

### 4.1. Ferramentas Utilizadas
- **Python**: Linguagem de programação utilizada para desenvolvimento.
- **Pygame**: Biblioteca utilizada para criação de jogos 2D.

### 4.2. Justificativas
- **Python**: Como foi exigido, o projeto todo foi feito em Python.
- **Pygame**: Popularidade e facilidade de uso para desenvolvimento de jogos simples.

## 5. 🧑‍💻 Divisão de Trabalho

### 5.1. Tarefas e Responsáveis
- **Andreywid e Jadiael - Desenvolvimento do Core do Jogo:** Implementação da lógica principal do jogo, incluindo o movimento do personagem e a coleta de cartões.
- **Andreywid - Design de Personagens e Cenários:** Criação e importação dos sprites para o jogador, mapa e os coletáveis.
- **Todos - Mecânicas de Jogo:** Implementação de colisões, itens coletáveis e condições de vitória/derrota.
- **João Victor - Interface de Usuário:** Design dos menus, telas de início e de fim de jogo.
- **Victor e Mário - Teste e Depuração:** Identificação e correção de bugs, otimização do desempenho.
- **Todos - Coordenação e Revisões:** Revisão de código e integração das contribuições individuais no GitHub.

## 6. 🧠 Conceitos Utilizados

### 6.1. Programação Orientada a Objetos (OOP)
- **Classes e Objetos**: Implementação das classes `Player`, `Level`, `Game`, `Collectible`, `CameraGroup` e `Tile`.

### 6.2. Estruturas de Dados
- **Listas**: Utilizadas para gerenciar coletáveis.

### 6.3. Tratamento de Eventos
- **Eventos do Pygame**: Controle de entradas do usuário e eventos do jogo.

## 7. 🚧 Desafios e Lições Aprendidas

### 7.1. Desafios Enfrentados 
- **Movimentação e Colisão:** Ajustar a movimentação dos personagens e a detecção de colisões.
- **Desempenho:** Garantir que o jogo funcione suavemente sem atrasos ou travamentos.
- **Integração de Som:** Sincronizar sons com eventos do jogo sem causar atrasos.
- **Gerenciamento de Memória:** Prevenir vazamentos de memória e otimizar o uso de recursos.
- **Teste em Diferentes Máquinas:** Garantir que o jogo funcione corretamente em diferentes configurações de hardware.
- **Merge de Código:** Resolver conflitos ao integrar contribuições de diferentes membros da equipe.
- **Interface de Usuário:** Criar uma interface intuitiva para o usuário.

#### 7.1.1. Maior Erro Cometido
- **Erro**: Inicialmente, não organizamos bem a estrutura do projeto.
- **Solução**: Reestruturamos o projeto, separando responsabilidades em diferentes módulos.

#### 7.1.2. Maior Desafio Enfrentado
- **Desafio**: Implementação de colisões entre o jogador e os inimigos.
- **Solução**: Estudamos a documentação do Pygame e aplicamos testes iterativos para ajustar a lógica.

### 7.2. Lições Aprendidas
- **Planejamento**: A importância de planejar a estrutura do projeto antes de começar a programar.
- **Trabalho em Equipe**: Como trabalhar em equipe, dividindo tarefas e integrando diferentes partes do código.
- **Conhecimento Técnico**: Melhor entendimento de Pygame e dos conceitos de OOP.

# Guidelines de Contribuição

## Mensagens de Commit

Utilizamos uma convenção que fornece um conjunto de regras para formular uma estrutura de mensagem de commit consistente da seguinte forma:

```
<type>[optional scope]: <description>

[optional body]
```

O tipo do commit pode ser:

- `feat` – uma nova funcionalidade é introduzida com as mudanças.
- `fix` – ocorreu uma correção de bug.
- `refactor` – código refatorado que não corrige um bug nem adiciona uma funcionalidade.
- `docs` – atualizações na documentação, como o README ou outros arquivos markdown.
- `style` – mudanças que não afetam o significado do código, provavelmente relacionadas à formatação do código, como espaços em branco, pontos e vírgulas ausentes, e assim por diante.

A linha de assunto do tipo de commit deve ser toda em letras minúsculas com um limite de 75 caracteres. Além disso, o corpo opcional do commit deve ser usado para fornecer mais detalhes que não cabem nas limitações de caracteres da descrição da linha de assunto.

## Criação de Branches

Uma branch do git deve começar com uma categoria. Escolha uma destas: `feature`, `bugfix`, ou `test`.

- `feature` é para adicionar, refatorar ou remover uma funcionalidade.
- `bugfix` é para corrigir um bug.
- `test` é para experimentação.

Após a categoria, deve haver um "/" seguido por uma descrição que resume o propósito desta branch específica. Esta descrição deve ser curta e em `kebab-case`. Para resumir, siga este padrão ao criar branches:

```
git branch <category/description-in-kebab-case>
```

Exemplos:

- Você precisa adicionar, refatorar ou remover uma funcionalidade: `git branch feature/create-new-button-component`
- Você precisa corrigir um bug: `git branch bugfix/button-overlap-form-on-mobile`
- Você precisa experimentar algo: `git branch test/refactor-components-with-atomic-design`
