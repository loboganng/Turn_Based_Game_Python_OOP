# Jogo de Batalha em Turnos (Python)

Este é um projeto simples em Python que simula uma batalha em turnos entre um herói controlado pelo jogador e um inimigo controlado pelo computador.  
O objetivo deste projeto é praticar Programação Orientada a Objetos (POO) com conceitos como herança, encapsulamento e polimorfismo.

## Tecnologias utilizadas
- Python 3.x
- Biblioteca padrão random

## Funcionalidades
- Criar personagens com atributos de nome, vida e nível  
- O herói possui uma habilidade especial além do ataque comum  
- O inimigo possui um tipo específico  
- Sistema de batalha por turnos, com ataque normal e ataque especial  
- O jogo termina quando a vida de um dos personagens chega a 0  

## Estrutura do Código
- Personagem: Classe base (nome, vida, nível)  
- Heroi: Herda de Personagem e adiciona habilidades especiais  
- Inimigo: Herda de Personagem e adiciona o tipo do inimigo  
- Jogo: Classe que controla a batalha  

## Como rodar o projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repo.git
   ```

2. Acesse a pasta do projeto:
   ```bash
   cd nome-do-repo
   ```

3. Execute o jogo:
   ```bash
   python jogo.py
   ```

## Exemplo de execução

```
Iniciando batalha!

Detalhes dos Personagens
Nome: Herói 
Vida: 100 
Nível: 5
Habilidade: Super Força

Nome: Morcego 
Vida: 50 
Nível: 3
Tipo: Voador

Pressione Enter para atacar...
Escolha (1 - Ataque Normal, 2 - Ataque Especial):
```

## Contribuição
Este é um projeto de estudo, mas sugestões de melhorias são bem-vindas.
