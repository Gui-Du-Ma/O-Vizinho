import pygame

from pathlib import Path

# =========================================================

# CONFIGURAÇÕES

# =========================================================

WIDTH = 1000

HEIGHT = 700

FPS = 60

# EFEITO DE PISCAR

FLASH_DURATION = 0.08

FLASH_COUNT = 3

BASE_DIR = Path(__file__).resolve().parent

ASSETS_DIR = BASE_DIR / "assets"

GAME_TITLE = "GIBÃO — AS CINCO NOITES"

TEXT_SPEED = 0.035

# ÁUDIO
BACKGROUND_MUSIC = "music.mp3"
RAFAEL_VOICE_SOUND = "sans.mp3"  # Som curtinho usado enquanto Rafael fala.

#DIMENSOES
DIALOGUE_HEIGHT = 200

DIALOGUE_MARGIN = 25

BLACK = (0, 0, 0)

WHITE = (255, 255, 255)

DIALOGUE_BG = (15, 15, 15)

DIALOGUE_BORDER = (100, 100, 100)

TEXT_COLOR = (235, 235, 235)

NAME_COLOR = (255, 220, 100)

# =========================================================

# FUNÇÕES AUXILIARES

# =========================================================

def load_image(path):

    try:

        return pygame.image.load(path).convert_alpha()

    except pygame.error as e:

        print()

        print("====================================")

        print("ERRO AO CARREGAR IMAGEM")

        print("Arquivo:", path)

        print("Existe?", path.exists())

        print("Erro:", e)

        print("====================================")

        print()

        return None

def load_animation(filenames):

    frames = []

    for filename in filenames:

        image = load_image(

            ASSETS_DIR / filename

        )

        if image is not None:

            frames.append(image)

    return frames

def draw_background(screen, image):

    if image is None:

        screen.fill(BLACK)

        return

    background = pygame.transform.smoothscale(

        image,

        (WIDTH, HEIGHT)

    )

    screen.blit(

        background,

        (0, 0)

    )

def draw_animation(screen, frames, index):

    if not frames:

        return

    if index >= len(frames):

        index = 0

    frame = frames[index]

    animation = pygame.transform.smoothscale(

        frame,

        (WIDTH, HEIGHT)

    )

    screen.blit(

        animation,

        (0, 0)

    )

def draw_character(screen, image, side):

    if image is None:

        return

    max_width = 230

    max_height = 320

    image_width, image_height = image.get_size()

    scale = min(

        max_width / image_width,

        max_height / image_height

    )

    new_width = int(

        image_width * scale

    )

    new_height = int(

        image_height * scale

    )

    character = pygame.transform.smoothscale(

        image,

        (new_width, new_height)

    )

    if side == "right":

        x = WIDTH - new_width - 70

    else:

        x = 70

    y = (

        HEIGHT

        - DIALOGUE_HEIGHT

        - new_height

        + 20

    )

    screen.blit(

        character,

        (x, y)

    )

def draw_dialogue_box(

    screen,

    speaker,

    text,

    text_font,

    name_font,

    text_finished

):

    box_x = DIALOGUE_MARGIN

    box_y = (

        HEIGHT

        - DIALOGUE_HEIGHT

        - DIALOGUE_MARGIN

    )

    box_width = WIDTH - (

        DIALOGUE_MARGIN * 2

    )

    box_height = DIALOGUE_HEIGHT

    # =====================================================

    # CAIXA TRANSPARENTE

    # =====================================================

    dialogue_surface = pygame.Surface(

        (box_width, box_height),

        pygame.SRCALPHA

    )

    dialogue_surface.fill(

        (15, 15, 15, 190)

    )

    screen.blit(

        dialogue_surface,

        (box_x, box_y)

    )

    # =====================================================

    # BORDA

    # =====================================================

    pygame.draw.rect(

        screen,

        DIALOGUE_BORDER,

        (

            box_x,

            box_y,

            box_width,

            box_height

        ),

        2

    )

    # =====================================================

    # NOME

    # =====================================================

    if speaker:

        name_surface = name_font.render(

            speaker,

            True,

            NAME_COLOR

        )

        screen.blit(

            name_surface,

            (

                box_x + 25,

                box_y + 18

            )

        )

    # =====================================================

    # TEXTO

    # =====================================================

    text_x = box_x + 25

    text_y = box_y + 70

    max_width = box_width - 50

    words = text.split(" ")

    lines = []

    current_line = ""

    for word in words:

        test_line = current_line

        if test_line:

            test_line += " "

        test_line += word

        if text_font.size(

            test_line

        )[0] <= max_width:

            current_line = test_line

        else:

            if current_line:

                lines.append(

                    current_line

                )

            current_line = word

    if current_line:

        lines.append(

            current_line

        )

    line_height = (

        text_font.get_height()

        + 5

    )

    for i, line in enumerate(lines):

        surface = text_font.render(

            line,

            True,

            TEXT_COLOR

        )

        screen.blit(

            surface,

            (

                text_x,

                text_y + i * line_height

            )

        )

    # =====================================================

    # INDICADOR DE CONTINUAR

    # =====================================================

    if text_finished:

        arrow = "▼"

        arrow_surface = text_font.render(

            arrow,

            True,

            WHITE

        )

        arrow_rect = arrow_surface.get_rect(

            bottomright=(

                box_x + box_width - 20,

                box_y + box_height - 15

            )

        )

        screen.blit(

            arrow_surface,

            arrow_rect

        )

# =========================================================

# CENAS

# =========================================================

SCENES = [

    # =====================================================

    # PRÓLOGO

    # =====================================================

    {

        "name": "prologo",

        "title": "",

        "background": "casa.png",

        "dialogues": [

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Meu nome é Bob."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Eu moro sozinho em uma casa pequena no meio do interior."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Tenho uma casa simples, um galinheiro e algumas galinhas."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Minha vida sempre foi tranquila."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Até aquela semana."

            }

        ]

    },

    # =====================================================

    # DIA 1

    # =====================================================

    {

        "name": "dia_1",

        "title": "DIA 1",

        "dialogues": [

            {

                "background": "quintalPF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Uma das minhas galinhas desapareceu."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Eu encontrei algumas penas perto da cerca."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Provavelmente foi um coiote."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Vou reforçar essa cerca."

            },

            {

                "background": "RtortoPF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Enquanto eu trabalhava, percebi alguém do outro lado da rua."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Ah, aquele cara denovo.",

                "animation": [

                    "RGwave1PF.png",

                    "RGwave2PF.png"

                ],

                "animation_speed": 0.50

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "..."

            },

            {

                "background": "RmaocruzadaPF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Era meu vizinho, Rafael.",

                "stop_animation": True

            }

        ]

    },

    # =====================================================

    # NOITE 1

    # =====================================================

    {

        "name": "noite_1",

        "title": "NOITE 1",

        "dialogues": [

            {

                "background": "bob.png",

                "speaker": "",

                "character": "bob.png",

                "side": "left",

                "text": "Clack.",

                "sound_once": "clack.mp3"

            },

            {

                "background": "quartoPF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Ouvi alguma coisa vindo do galinheiro."

            },

            {

                "background": "quintaljanela.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Deixa eu ver.."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "...",

                "animation": [

                    "RGrasteja1PF.png",

                    "RGrasteja2PF.png",

                    "RGrasteja3PF.png",

                    "RGrasteja4PF.png"

                ],

                "animation_speed": 0.50,

                "animation_blocking": True,

                "sound_once": "grass.mp3"

            },

            {

                "background": "quintaljanela.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "o que era aquilo??",

                "stop_animation": True

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Uma sombra passou pela janela."

            },

            {

                "background": "quartoPF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Talvez eu esteja ficando paranoico."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Vou voltar a dormir.."

            }

        ]

    },

    # =====================================================

    # DIA 2

    # =====================================================

    {

        "name": "dia_2",

        "title": "DIA 2",

        "dialogues": [

             {

                "background": "quintal1PF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Quando acordei, algumas galinhas havia desaparecido"

            },

             {

                "background": "quintal1PF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Estou começando a achar que não foi um Coiote.."

            },

            {

                "background": "RamenPF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Hoje eu vi Rafael carregando um saco enorme."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "O que tem aí?"

            },

            {

                "speaker": "Rafael",

                "character": "Rafael.png",

                "side": "right",

                "text": "Amendoim. Vinte e cinco quilos."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Vinte e cinco quilos de amendoim?"

            },

            {

                "speaker": "Rafael",

                "character": "Rafael.png",

                "side": "right",

                "text": "É para o Gibão."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Gibão?"

            },

            {

                "speaker": "Rafael",

                "character": "Rafael.png",

                "side": "right",

                "text": "Você não conhece o gibaonismo?"

            },

            {

                "speaker": "Rafael",

                "character": "Rafael.png",

                "side": "right",

                "text": "O Gibão protege as casas do que vive lá fora."

            },

            {

                "speaker": "Rafael",

                "character": "Rafael.png",

                "side": "right",

                "text": "Se quiser, posso te dar um pouco de amendoim."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Não, obrigado."

            },

            {

                "background": "quintalPF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Mesmo assim, coloquei um pouco perto do galinheiro."

            }

        ]

    },

    # =====================================================

    # NOITE 2

    # =====================================================

    {

        "name": "noite_2",

        "title": "NOITE 2",

        "dialogues": [

            {

                "background": "bob.png",

                "speaker": "",

                "character": "bob.png",

                "side": "left",

                "text": "03:12."

            },

            {

                "background": "quartoPF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Eu acordei com um barulho."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "background": "Rgalinhamao1PF.png",

                "side": "left",

                "text": "Quando olhei pela janela, vi Rafael no meu quintal."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Ele estava segurando uma das minhas galinhas."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "...",

                "animation": [

                "Rgalinhamao2PF.png",

                "Rgalinhamao2PF.png",

                "Rgalinhamao2PF.png",

                "RGgalinhamao1PF.png",

                "RGgalinhamao2PF.png",

                "RGgalinhamao3PF.png"

                ],

                "animation_speed": 0.50,

                "animation_blocking": True,

                "sound_once": "grass.mp3"

            },

            {

                "background": "quintaljanela.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Ele correu de volta para casa."

            },

            {

                "background": "galinheiroPF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Quando fui até o galinheiro, a galinha tinha desaparecido."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "O amendoim estava espalhado pelo chão."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Foi ele."

            }

        ]

    },

    # =====================================================

    # DIA 3

    # =====================================================

    {

        "name": "dia_3",

        "title": "DIA 3",

        "dialogues": [

            {

                "background": "bob.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Comecei a observar Rafael."

            },

            {

                "background": "dentroPF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Comprei bastante amendoim e fiquei em casa."

            },

            {

                "background": "RbisbilhotandoPF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "As vezes eu ouvia ele falando sozinho",

                "sound_loop": "murmurando.mp3"

            },

            {

                "background": "pcPF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Comecei a pesquisar sobre o tal gibaonismo."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Encontrei uma frase estranha."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Amendoim alimenta aquilo que protege a casa."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Quando o Gibão é invocado, os animais domésticos devem permanecer dentro do círculo de proteção."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "...",

                "animation": [

                    "RGcorrendo1PF.png",

                    "RGcorrendo2PF.png",

                    "RGcorrendo3PF.png",

                ],

                "animation_speed": 0.50,

                "animation_blocking": True

            },

            {

                "background": "quintaljanela.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Então vi Rafael correndo carregando outra galinha para dentro da casa dele."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Eu não gritei."

            }

        ]

    },

    # =====================================================

    # NOITE 3

    # =====================================================

     #{

        #"name": "hora_title2",

        #"title": "2:47",

        #"dialogues": [

        #]

    #},

    {

        "name": "noite_3",

        "title": "NOITE 3",

        "dialogues": [

            {

                "background": "bob.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "02:47."

            },

            {

                "background": "quartoPF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Eu ouvi uma respiração pesada.",

                "sound_loop": "breathe.mp3"

            },

            {

                "background": "vultoPF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Olhei para o galinheiro."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Uma silhueta muito alta estava atrás dele."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Eu pisquei.",

                "flash_after": True

            },

            {

                "background": "quintaljanela.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Ela desapareceu."

            },

            {
                "background": "Rgalinhamao2PF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Rafael apareceu."

            },

            {

                "speaker": "Rafael",

                "character": "rafael.png",

                "side": "right",

                "text": "Estou tentando proteger elas."

            },

            {
                "background": "quartoPF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Ele levou as galinhas restantes para dentro da casa dele."

            }

        ]

    },

    # =====================================================

    # DIA 4

    # =====================================================

    {

        "name": "dia_4",

        "title": "DIA 4",

        

        "dialogues": [

            {
                "background": "casarafaPF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Eu decidi confrontar Rafael."

            },

            {
                "background": "RportaPF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Por que você está levando minhas galinhas?"

            },

            {

                "speaker": "Rafael",

                "character": "rafael.png",

                "side": "right",

                "text": "Eu não estou tentando machucar elas."

            },
            {
            
                "speaker": "Rafael",
            
                "character": "rafael.png",
            
                "side": "right",
            
                "text": "Estou tentando proteger você."
            
            },
                    ]
    },  

    {
    
            "name": "dia_42",
    
            "title": "",
    
            
    
            "dialogues": [

            {
                "background": "gib1PF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "A casa dele estava cheia de sacos de amendoim."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Havia símbolos religiosos espalhados pelas paredes."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "E no centro da sala havia uma escultura enorme."

            },

            {
                "background": "gib2PF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Era o Gibão."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Tinha braços compridos, um rosto quase humano e um sorriso assustador."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Por um instante, tive a impressão de que ele estava olhando para mim."

            }

        ]

    },

    # =====================================================

    # NOITE 4

    # =====================================================

    {

        "name": "noite_4",

        "title": "NOITE 4",

        

        "dialogues": [

            {
                "background": "bob.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "03:17."

            },

            {
                "background": "quartoPF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Alguém bateu na porta."

            },

            {
                "background": "Rseg1PF.png",

                "speaker": "Rafael",

                "character": "rafael.png",

                "side": "right",

                "text": "Bob!"

            },

            {

                "speaker": "Rafael",

                "character": "rafael.png",

                "side": "right",

                "text": "Não saia."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Rafael estava segurando um bastão."

            },

            {
                "background": "Rseg2PF.png",

                "speaker": "Rafael",

                "character": "rafael.png",

                "side": "right",

                "text": "Hoje ele veio procurar você."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Então tudo ficou escuro."

            }

        ]

    },

    # =====================================================

    # DIA 5

    # =====================================================

    {

        "name": "dia_5",

        "title": "DIA 5",

        

        "dialogues": [

            {
                "background": "casarafaPF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Rafael saiu de casa."

            },

            {
                "background": "gib2PF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Eu entrei na casa dele."

            },

            {

                "background": "porao1PF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Encontrei uma sala secreta."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Havia uma espada."

            },

            {
                "background": "porao2PF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Fotos de várias casas com galinheiros."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "E várias anotações."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "elas diziam: QUINTA NOITE."

            },

            {
                "background": "porao3PF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Então encontrei uma foto antiga."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Era a minha casa."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "No verso estava escrito:"

            },

            {
                "background": "porao4PF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "ELE SEMPRE VOLTA."

            },

            {

                "speaker": "Rafael",

                "character": "rafael.png",

                "side": "right",

                "text": "Bob?"

            }

        ]

    },

    # =====================================================

    # NOITE 5 — FINAL

    # =====================================================

    {

        "name": "noite_5_final",

        "title": "NOITE 5",

        "dialogues": [

            {
                "background": "FvoPF.png",

                "speaker": "Rafael",

                "character": "rafael.png",

                "side": "right",

                "text": "Meu avô morava nessa casa."

            },

            {
                "background": "FquadroPF.png",

                "speaker": "Rafael",

                "character": "rafael.png",

                "side": "right",

                "text": "Ele também criava galinhas."

            },

            {

                "speaker": "Rafael",

                "character": "rafael.png",

                "side": "right",

                "text": "Na quinta noite, todas desapareceram."

            },

            {
                "background": "Fvo1PF.png",

                "speaker": "Rafael",

                "character": "rafael.png",

                "side": "right",

                "text": "E meu avô também."

            },

            {

                "speaker": "Rafael",

                "character": "rafael.png",

                "side": "right",

                "text": "Minha família passou décadas tentando descobrir o que aconteceu."

            },

            {
                "background": "Fconv1PF.png",

                "speaker": "Rafael",

                "character": "rafael.png",

                "side": "right",

                "text": "O gibaonismo é uma forma de proteção."

            },

            {

                "speaker": "Rafael",

                "character": "rafael.png",

                "side": "right",

                "text": "Os amendoins, as câmeras e a espada ajudam a manter aquilo longe."

            },

            {
                "background": "camgalin1PF.png",

                "speaker": "Rafael",

                "character": "rafael.png",

                "side": "right",

                "text": "As galinhas fazem barulho quando ele está perto."

            },

            {
                "background": "Fconv1PF.png",

                "speaker": "Rafael",

                "character": "rafael.png",

                "side": "right",

                "text": "Eu estava tentando proteger você."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Então ele é o Gibão?"

            },

            {

                "speaker": "Rafael",

                "character": "rafael.png",

                "side": "right",

                "text": "Não."

            },

            {

                "speaker": "Rafael",

                "character": "rafael.png",

                "side": "right",

                "text": "Gibão é o que está tentando manter ele longe."

            },

            {
                "background": "toc2PF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "A luz começou a piscar."

            },

            {
                "background": "toc1PF.png",

                "speaker": "",

                "character": "bob.png",

                "side": "left",

                "text": "Toc. Toc.",

                "sound_once": "batida.mp3"

            },

            {
                "background": "conv2PF.png",

                "speaker": "Rafael",

                "character": "rafael.png",

                "side": "right",

                "text": "Não faça barulho."

            },

            {

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "As galinhas começaram a gritar.",

                "sound_loop": "galinha.mp3"

            },

            {
                "background": "conv3PF.png",

                "speaker": "Bob",

                "character": "bob.png",

                "side": "left",

                "text": "Então tudo parou."

            }

        ]

    },

    # =====================================================

    # PÓS-CRÉDITOS

    # =====================================================

    {

        "name": "pos_creditos",

        "title": "Dia 6.",

        "background": None,

        "dialogues": [

            {

                "speaker": "",

                "character": None,

                "side": "left",

                "text": "AS GALINHAS FORAM DEVOLVIDAS NA MANHÃ SEGUINTE."

            },

            {

                "speaker": "",

                "character": None,

                "side": "left",

                "text": "RAFAEL NUNCA MAIS FOI VISTO."

            },

            {

                "speaker": "",

                "character": None,

                "side": "left",

                "text": "BOB CONTINUOU MORANDO NA CASA."

            },

            {

                "speaker": "",

                "character": None,

                "side": "left",

                "text": "ELE AINDA COMPRA AMENDOIM."

                

            }

        ]

    }

]

# =========================================================

# CLASSE DO JOGO

# =========================================================

class Game:

    def __init__(self):

        self.flashing = False

        self.flash_timer = 0

        self.flash_count = 0

        self.flash_state = False

        self.flash_next_dialogue = False

        # SOM DO DIÁLOGO

        self.dialogue_sound = None

        self.dialogue_sound_channel = None
        self.dialogue_one_shot_sound = None
        self.rafael_voice_sound = None
        self.rafael_voice_channel = None
        self.last_voice_character = 0

        pygame.init()

        # MÚSICA DE FUNDO DO JOGO INTEIRO (loop)
        # Troque BACKGROUND_MUSIC pelo nome do seu arquivo em assets.
        music_path = ASSETS_DIR / BACKGROUND_MUSIC
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init()
            pygame.mixer.music.load(str(music_path))
            pygame.mixer.music.play(-1)
        except (pygame.error, OSError) as e:
            print("Não foi possível carregar a música de fundo:", music_path)
            print("Erro:", e)

        # VOZ CURTA DO RAFAEL, REPETIDA ENQUANTO O TEXTO É DIGITADO
        if pygame.mixer.get_init():
            try:
                voice_path = ASSETS_DIR / RAFAEL_VOICE_SOUND
                self.rafael_voice_sound = pygame.mixer.Sound(str(voice_path))
                self.rafael_voice_channel = pygame.mixer.Channel(1)
            except (pygame.error, OSError) as e:
                print("Não foi possível carregar a voz do Rafael:", ASSETS_DIR / RAFAEL_VOICE_SOUND)
                print("Erro:", e)

        self.screen = pygame.display.set_mode(

            (WIDTH, HEIGHT)

        )

        pygame.display.set_caption(

            GAME_TITLE

        )

        self.clock = pygame.time.Clock()

        # =================================================

        # FONTES

        # =================================================

        self.text_font = pygame.font.Font(

            None,

            31

        )

        self.name_font = pygame.font.Font(

            None,

            35

        )

        # =================================================

        # CENA ATUAL

        # =================================================

        self.scene_index = 0

        self.dialogue_index = 0

        # =================================================

        # TEXTO

        # =================================================

        self.full_text = ""

        self.visible_text = ""

        self.text_timer = 0

        self.text_finished = False

        # =================================================

        # JOGO

        # =================================================

        self.running = True

        # =================================================

        # IMAGENS

        # =================================================

        self.background = None

        self.character = None

        self.character_side = "left"

        # =================================================

        # FALANTE

        # =================================================

        self.speaker = ""

        # =================================================

        # ANIMAÇÃO

        # =================================================

        self.animation_frames = []

        self.animation_index = 0

        self.animation_timer = 0

        self.animation_speed = 0.15

        self.animation_playing = False

        self.animation_frames = []

        self.animation_index = 0

        self.animation_timer = 0

        self.animation_speed = 0.15

        self.animation_playing = False

        self.animation_blocking = False

        self.animation_visible = False

        # =================================================

        # TRANSIÇÃO

        # =================================================

        self.transitioning = False

        self.transition_alpha = 0

        self.transition_speed = 500

        self.transition_phase = "none"

        self.next_scene_index = 0

        self.scene_title = ""

        self.title_timer = 0

        self.title_duration = 1.8

        # =================================================

        # CARREGA PRIMEIRA CENA

        # =================================================

        self.load_scene()

    # =====================================================

    # EFEITO DE PISCAR

    # =====================================================

    def start_flash(self):

        self.flashing = True

        self.flash_timer = 0

        self.flash_count = 0

        self.flash_state = True

        self.flash_next_dialogue = True

    def update_flash(self, dt):

        if not self.flashing:

            return

        self.flash_timer += dt

        if self.flash_timer >= FLASH_DURATION:

            self.flash_timer -= FLASH_DURATION

            self.flash_state = not self.flash_state

            if self.flash_state:

                self.flash_count += 1

            if self.flash_count >= FLASH_COUNT:

                self.flashing = False

                self.flash_state = False

                if self.flash_next_dialogue:

                    self.flash_next_dialogue = False

                    self.dialogue_index += 1

                    self.load_dialogue()

    def advance_dialogue(self):

        if self.flashing or self.transitioning:

            return

        if self.animation_blocking and self.animation_playing:

            return

        if not self.text_finished:

            self.visible_text = self.full_text

            self.text_finished = True

            return

        dialogue = self.scene.get("dialogues", [])[self.dialogue_index]

        if dialogue.get("flash_after", False):

            self.start_flash()

            return

        self.dialogue_index += 1

        self.load_dialogue()

    # =====================================================

    # CARREGAR CENA

    # =====================================================

    def load_scene(self):

        if self.scene_index >= len(SCENES):

            self.running = False

            return

        self.scene = SCENES[

            self.scene_index

        ]

        # =================================================

        # FUNDO DA CENA

        # =================================================

        background_name = self.scene.get(

            "background"

        )

        if background_name:

            self.background = load_image(

                ASSETS_DIR / background_name

            )

        else:

            self.background = None

        # =================================================

        # RESET DO DIÁLOGO

        # =================================================

        self.dialogue_index = 0

        # =================================================

        # CARREGA DIÁLOGO

        # =================================================

        self.load_dialogue()

    # =====================================================

    # CARREGAR DIÁLOGO

    # =====================================================

    def stop_dialogue_sound(self):

        if self.dialogue_sound_channel is not None:

            self.dialogue_sound_channel.stop()

            self.dialogue_sound_channel = None

        self.dialogue_sound = None

    def load_dialogue(self):

        # Para o som do diálogo anterior

        self.stop_dialogue_sound()

        dialogues = self.scene.get(

            "dialogues",

            []

        )

        # FIM DA CENA

        if self.dialogue_index >= len(dialogues):

            self.start_transition()

            return

        dialogue = dialogues[

            self.dialogue_index

        ]
        self.last_voice_character = 0

        # SOM EM LOOP DO DIÁLOGO (OPCIONAL)

        sound_name = dialogue.get("sound_loop")

        if sound_name:

            sound_path = ASSETS_DIR / sound_name

            try:

                self.dialogue_sound = pygame.mixer.Sound(str(sound_path))

                self.dialogue_sound_channel = self.dialogue_sound.play(-1)

            except (pygame.error, OSError) as e:

                print("Não foi possível carregar o som:", sound_path)

                print("Erro:", e)

                self.dialogue_sound = None

                self.dialogue_sound_channel = None

        # EFEITO SONORO DE UMA ÚNICA EXECUÇÃO (OPCIONAL)
        # Use "sound_once": "arquivo.wav" no diálogo desejado.
        sound_once_name = dialogue.get("sound_once")
        if sound_once_name:
            sound_once_path = ASSETS_DIR / sound_once_name
            try:
                self.dialogue_one_shot_sound = pygame.mixer.Sound(str(sound_once_path))
                self.dialogue_one_shot_sound.play()
            except (pygame.error, OSError) as e:
                print("Não foi possível carregar o efeito sonoro:", sound_once_path)
                print("Erro:", e)
                self.dialogue_one_shot_sound = None

        # TROCAR FUNDO

        background_name = dialogue.get(

            "background"

        )

        if background_name:

            self.background = load_image(

                ASSETS_DIR / background_name

            )

        # ANIMAÇÃO

        self.animation_blocking = False

        if "animation" in dialogue:

            animation_files = dialogue.get(

                "animation",

                []

            )

            self.animation_frames = load_animation(

                animation_files

            )

            self.animation_index = 0

            self.animation_timer = 0

            self.animation_speed = dialogue.get(

                "animation_speed",

                0.15

            )

            self.animation_blocking = dialogue.get(

                "animation_blocking",

                False

            )

            if self.animation_frames:

                self.animation_playing = True

            else:

                self.animation_playing = False

                self.animation_blocking = False

        # PARAR ANIMAÇÃO

        if dialogue.get("stop_animation", False):

            self.animation_playing = False

            self.animation_blocking = False

            self.animation_frames = []

            self.animation_index = 0

            self.animation_timer = 0

        # FALANTE

        self.speaker = dialogue.get(

            "speaker",

            ""

        )

        # TEXTO

        self.full_text = dialogue.get(

            "text",

            ""

        )

        self.visible_text = ""

        self.text_timer = 0

        self.text_finished = False

        # PERSONAGEM

        character_name = dialogue.get(

            "character"

        )

        if character_name:

            self.character = load_image(

                ASSETS_DIR / character_name

            )

        else:

            self.character = None

        # LADO DO PERSONAGEM

        self.character_side = dialogue.get(

            "side",

            "left"

        )

    # =====================================================

    # ATUALIZAR ANIMAÇÃO

    # =====================================================

    def update_animation(self, dt):

        if not self.animation_playing:

            return

        if not self.animation_frames:

            self.animation_playing = False

            self.animation_blocking = False

            return

        self.animation_timer += dt

        if self.animation_timer >= self.animation_speed:

            self.animation_timer = 0

            self.animation_index += 1

            # FIM DA ANIMAÇÃO

            if self.animation_index >= len(

                self.animation_frames

            ):


                if self.animation_blocking:

                    self.animation_playing = False

                    self.animation_blocking = False

                    self.dialogue_index += 1

                    self.load_dialogue()

                else:


                    self.animation_index = 0

    # =====================================================

    # COMEÇAR TRANSIÇÃO

    # =====================================================

    def start_transition(self):

        self.stop_dialogue_sound()

        self.transitioning = True

        self.transition_phase = "fade_out"

        self.transition_alpha = 0

        self.next_scene_index = (

            self.scene_index + 1

        )

        # =================================================

        # PARA ANIMAÇÃO AO TROCAR DE CENA

        # =================================================

        self.animation_playing = False

        self.animation_frames = []

        self.animation_index = 0

        self.animation_timer = 0

        # =================================================

        # PEGA TÍTULO DA PRÓXIMA CENA

        # =================================================

        if self.next_scene_index < len(SCENES):

            self.scene_title = SCENES[

                self.next_scene_index

            ].get(

                "title",

                ""

            )

        else:

            self.scene_title = "FIM"

        self.title_timer = 0

    # =====================================================

    # ATUALIZAR TRANSIÇÃO

    # =====================================================

    def update_transition(self, dt):

        if not self.transitioning:

            return

        # =================================================

        # FADE OUT

        # =================================================

        if self.transition_phase == "fade_out":

            self.transition_alpha += (

                self.transition_speed * dt

            )

            if self.transition_alpha >= 255:

                self.transition_alpha = 255

                self.transition_phase = "title"

                self.title_timer = 0

        # =================================================

        # TÍTULO

        # =================================================

        elif self.transition_phase == "title":

            self.title_timer += dt

            if self.title_timer >= self.title_duration:

                self.scene_index = (

                    self.next_scene_index

                )

                if self.scene_index < len(SCENES):

                    self.load_scene()

                    self.transition_phase = "fade_in"

                else:

                    self.running = False

        # =================================================

        # FADE IN

        # =================================================

        elif self.transition_phase == "fade_in":

            self.transition_alpha -= (

                self.transition_speed * dt

            )

            if self.transition_alpha <= 0:

                self.transition_alpha = 0

                self.transitioning = False

                self.transition_phase = "none"

    # =====================================================

    # EVENTOS

    # =====================================================

    def jump_to_day(self, day_number):

        """Pula diretamente para a cena inicial do dia escolhido."""

        scene_name = f"dia_{day_number}"

        for index, scene in enumerate(SCENES):

            if scene.get("name") == scene_name:

                self.stop_dialogue_sound()

                self.scene_index = index

                self.dialogue_index = 0

                # Cancela efeitos e transições em andamento.

                self.flashing = False

                self.flash_state = False

                self.flash_next_dialogue = False

                self.transitioning = False

                self.transition_phase = "none"

                self.transition_alpha = 0

                self.animation_playing = False

                self.animation_blocking = False

                self.animation_frames = []

                self.load_scene()

                print(f"Atalho ativado: DIA {day_number}")

                return

        print(f"Não encontrei uma cena para o DIA {day_number}.")

    def handle_event(self, event):

        # =================================================

        # FECHAR JANELA

        # =================================================

        if event.type == pygame.QUIT:

            self.running = False

        # =================================================

        # TECLADO

        # =================================================

        if self.flashing:

            return

        if event.type == pygame.KEYDOWN:

            # -------------------------------------------------

            # ESC

            # -------------------------------------------------

            if event.key == pygame.K_ESCAPE:

                self.running = False

            # ATALHO DE TESTE: SEGURE P + R E PRESSIONE 1 A 5

            if event.key in (

                pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,

                pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, pygame.K_KP5,

            ):

                keys = pygame.key.get_pressed()

                if keys[pygame.K_p] and keys[pygame.K_r]:

                    day_number = {

                        pygame.K_1: 1, pygame.K_2: 2, pygame.K_3: 3,
                        pygame.K_4: 4, pygame.K_5: 5,

                        pygame.K_KP1: 1, pygame.K_KP2: 2, pygame.K_KP3: 3,
                        pygame.K_KP4: 4, pygame.K_KP5: 5,

                    }[event.key]

                    self.jump_to_day(day_number)

                    return

            # -------------------------------------------------

            # ENTER OU ESPAÇO

            # -------------------------------------------------

            if event.key in (

                pygame.K_RETURN,

                pygame.K_SPACE

            ):

                self.advance_dialogue()

        # =================================================

        # MOUSE

        # =================================================

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                self.advance_dialogue()

    # =====================================================

    # TEXTO SENDO DIGITADO

    # =====================================================

    def update_text(self, dt):

        if self.text_finished:

            return

        if not self.full_text:

            self.text_finished = True

            return

        self.text_timer += dt

        characters_to_show = int(

            self.text_timer / TEXT_SPEED

        )

        self.visible_text = (

            self.full_text[

                :characters_to_show

            ]

        )

        # Efeito estilo Sans: o som curtinho se repete durante a fala do Rafael.
        if (
            self.speaker.lower() == "rafael"
            and self.rafael_voice_sound is not None
            and self.rafael_voice_channel is not None
            and characters_to_show > self.last_voice_character + 1
        ):
            new_character = self.full_text[min(characters_to_show - 1, len(self.full_text) - 1)]
            self.last_voice_character = characters_to_show
            if not new_character.isspace() and new_character not in ".,!?;:":
                self.rafael_voice_channel.play(self.rafael_voice_sound)

        if len(self.visible_text) >= len(

            self.full_text

        ):

            self.visible_text = (

                self.full_text

            )

            self.text_finished = True

    # =====================================================

    # DESENHAR TRANSIÇÃO

    # =====================================================

    def draw_transition(self):

        if not self.transitioning:

            return

        fade_surface = pygame.Surface(

            (WIDTH, HEIGHT)

        )

        fade_surface.fill(

            BLACK

        )

        fade_surface.set_alpha(

            int(self.transition_alpha)

        )

        self.screen.blit(

            fade_surface,

            (0, 0)

        )

        # =================================================

        # TÍTULO NO MEIO DA TELA

        # =================================================

        if self.transition_phase == "title":

            title_font = pygame.font.Font(

                None,

                60

            )

            title_surface = title_font.render(

                self.scene_title,

                True,

                WHITE

            )

            title_rect = title_surface.get_rect(

                center=(

                    WIDTH // 2,

                    HEIGHT // 2

                )

            )

            self.screen.blit(

                title_surface,

                title_rect

            )

    # =====================================================

    # DESENHAR

    # =====================================================

    def draw(self):

        # =================================================

        # FUNDO

        # =================================================

        draw_background(

            self.screen,

            self.background

        )

        # =================================================

        # ANIMAÇÃO

        # =================================================

        if self.animation_playing:

            draw_animation(

                self.screen,

                self.animation_frames,

                self.animation_index

            )

        # =================================================

        # PERSONAGEM

        # =================================================

        draw_character(

            self.screen,

            self.character,

            self.character_side

        )

        # =================================================

        # CAIXA DE DIÁLOGO

        # =================================================

        draw_dialogue_box(

            self.screen,

            self.speaker,

            self.visible_text,

            self.text_font,

            self.name_font,

            self.text_finished

        )

        # =================================================

        # FADE / TÍTULO

        # =================================================

        self.draw_transition()

        if self.flashing and self.flash_state:

            self.screen.fill((0, 0, 0))

        pygame.display.flip()

    # =====================================================

    # LOOP PRINCIPAL

    # =====================================================

    def run(self):

        while self.running:

            dt = self.clock.tick(

                FPS

            ) / 1000

            # =================================================

            # EVENTOS

            # =================================================

            for event in pygame.event.get():

                self.handle_event(

                    event

                )

            # =================================================

            # EFEITO DE PISCAR

            # =================================================

            self.update_flash(dt)

            # =================================================

            # TEXTO

            # =================================================

            if not self.transitioning and not self.flashing:

                self.update_text(

                    dt

                )

            # =================================================

            # ANIMAÇÃO

            # =================================================

            if not self.transitioning and not self.flashing:

                self.update_animation(

                    dt

                )

            # =================================================

            # TRANSIÇÃO

            # =================================================

            self.update_transition(

                dt

            )

            # =================================================

            # DESENHO

            # =================================================

            self.draw()

        self.stop_dialogue_sound()
        pygame.mixer.music.stop()

        pygame.quit()

# =========================================================

# INICIAR JOGO

# =========================================================

if __name__ == "__main__":

    game = Game()

    game.run()