# Battle in the Deep - Demo Version 1.0

Um jogo de sobrevivência subaquático desenvolvido em Python usando Pygame por Larissa Ferreira de Jesus

## 📖 Sobre o Jogo

Battle in the Deep é um jogo de ação onde você controla um submarino e deve sobreviver o máximo de tempo possível enfrentando ondas crescentes de inimigos nas profundezas do oceano.

## 🎮 Como Jogar

### Controles
- **W, A, S, D**: Movimentar o submarino
- **ESPAÇO**: Atirar
- **ENTER**: Confirmar seleções
- **↑/↓**: Navegar no menu
- **ESC**: Voltar (na tela de scores)
- **C**: Limpar scores (na tela de scores)

### Objetivo
- Sobreviva o máximo de tempo possível
- Derrote inimigos para continuar vivo
- Seu score é baseado no tempo de sobrevivência
- Evite colisões com inimigos para não perder vida

## 🚀 Instalação e Execução

### Pré-requisitos
- Python 3.x
- Pygame

### Instalação
1. Clone ou baixe o projeto
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Executar o Jogo
```bash
python Main.py
```

## 📁 Estrutura do Projeto

```
GameAula/
├── Main.py                 # Arquivo principal
├── README.md              # Este arquivo
├── requirements.txt       # Dependências
├── asset/                 # Recursos do jogo
│   ├── *.png             # Sprites e imagens
│   ├── PressStart2P-Regular.ttf  # Fonte personalizada
│   ├── ShootSound.wav    # Som de tiro
│   └── underwater.wav    # Música de fundo
├── code/                  # Código fonte
│   ├── Game.py           # Classe principal do jogo
│   ├── Menu.py           # Menu principal
│   ├── Level.py          # Lógica do nível
│   ├── Player.py         # Classe do jogador
│   ├── Enemy.py          # Classe dos inimigos
│   ├── PlayerNameScreen.py  # Tela de entrada do nome
│   ├── ScoreScreen.py    # Tela de pontuações
│   └── ...               # Outros arquivos do jogo
└── score/                 # Arquivos de pontuação
    └── scores.db         # Banco de dados SQLite com scores
```

## 🎯 Funcionalidades

- **Sistema de Menu**: Navegação intuitiva entre telas
- **Entrada de Nome**: Validação mínima de 3 caracteres
- **Sistema de Score**: Salvamento automático das melhores pontuações
- **Efeitos Visuais**: Texto com sombra e efeitos de dano
- **Áudio**: Sons de tiro e música de fundo
- **Dificuldade Progressiva**: Inimigos aumentam com o tempo
- **Sistema de Vida**: Invencibilidade temporária após dano

## 🎨 Recursos Visuais

- Fonte personalizada Press Start 2P
- Efeitos de sombra nos textos
- Animações de dano no jogador
- Interface colorida e temática

## 🔊 Recursos de Áudio

- Som de tiro realista
- Música de fundo ambiente subaquático
- Sistema de áudio integrado com Pygame

## 🏆 Sistema de Pontuação

- Score baseado em tempo de sobrevivência
- Top scores salvos automaticamente
- Opção para limpar histórico de pontuações

## 📝 Versão Demo

Esta é uma versão demo do jogo com funcionalidades limitadas. Futuras versões podem incluir:
- Mais níveis
- Novos tipos de inimigos
- Power-ups
- Modos de jogo adicionais

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**: Linguagem principal
- **Pygame**: Engine de jogos 2D
- **SQLite**: Banco de dados para armazenamento de scores

## 👨‍💻 Desenvolvimento

Jogo desenvolvido como projeto educacional utilizando conceitos de:
- Programação Orientada a Objetos
- Padrões de Design (Factory, Mediator)
- Gerenciamento de Estados
- Manipulação de Eventos
- Renderização 2D

## 📄 Licenças

### Recursos de Áudio
- **Underwater / space soundscape** by SamsterBirdies  
  https://freesound.org/s/612175/  
  License: Creative Commons 0

- **Bubble Pop** by YehawSnail 
  https://freesound.org/s/683587/ 
  License: Creative Commons 0

---

**Divirta-se jogando Battle in the Deep!** 🌊🚢