readme = """# Meu Jogo — estrutura narrativa em Pygame

## Instalação

No CMD, dentro da pasta do projeto:

    python -m pip install pygame

Depois:

    python main.py

## Imagem da casa

Coloque sua imagem de 651x500 em:

    assets/casa.png

O jogo mantém a proporção da imagem e faz ela cobrir a tela.

## Onde editar o jogo

Abra `main.py`.

A parte mais importante para criar o roteiro é `SCENES`.

Exemplo:

    SCENES = [
        {
            "name": "cena_1",
            "background": "casa.png",
            "dialogues": [
                {
                    "speaker": "Guilherme",
                    "text": "Olá."
                },
                {
                    "speaker": "???",
                    "text": "Quem é você?"
                },
            ],
        },
    ]

### Criar uma nova cena

Adicione outro bloco dentro de `SCENES`:

    {
        "name": "cena_2",
        "background": "quarto.png",
        "dialogues": [
            {
                "speaker": "Guilherme",
                "text": "Agora estou em outro lugar."
            },
        ],
    }

Coloque `quarto.png` dentro de `assets`.

## Controles

ENTER ou ESPAÇO:
- durante o texto: completa a fala
- depois que a fala terminou: vai para a próxima fala

ESC:
- fecha o jogo

## Próximas coisas que podem ser adicionadas

- sprites de personagens
- personagens aparecendo e desaparecendo
- posições diferentes dos personagens
- expressões
- troca de cenário
- escolhas do jogador
- múltiplos finais
- efeitos sonoros
- música
- transições
- efeitos de tela
- save/load
- sistema de capítulos
"""