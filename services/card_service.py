"""Servicio que devuelve datos para las cards.
Aquí puedes reemplazar la implementación por consultas a BD, llamadas a APIs o lógica de negocio.
"""

from typing import List, Dict


def get_cards() -> List[Dict]:
    """Devuelve una lista de diccionarios con la estructura que espera la plantilla.

    Cada diccionario puede tener las claves:
    - title (str)
    - description (str)
    - summary (str)  # clave opcional
    - image (str) ruta relativa en `static/` (ej: 'images/card1.jpg')
    - link (str)
    - button_text (str)
    """
    cards = [
        {
            'title': 'Estrategas invisibles, vedugos del silencio',
            'description': 'NOXKORE es sigilo, trampa y precisión encubierta.Se mueven como sombras; piensan como maestros.Ganan desde la oscuridad, nunca desde el ruido.Si los ves... ya es tarde.',
            'summary':'Juego mental, rotaciones letales, engaño táctico.Dominan MOBAs, Siege y arenas con visión estratégica.Juegan con tu mente, no con tus mecánicas.',
            'image': 'images/noxkore.png',
            'link': '#',
            'button_text': 'Saber Más'
        },
        {
            'title': 'Saboteadores del meta. Arquitectos del caos',
            'description': 'Krypta no sigue el meta. Lo hackea, lo explota.Su estilo es caos adaptativo, genialidad espontánea.Nunca verás dos partidas iguales. Improvisan victoria desde el error.',
            'summary':'Estrategias rotas, picks absurdos, juego fluido.Ideales para modos alternos y torneos flex.Cuando pierden, crean. Cuando ganan, rompen.',
            'image': 'images/kryptax.png',
            'link': '#',
            'button_text': 'Saber Más'
        },
        {
            'title': 'Precisión artificial. Frialdad absoluta',
            'description': 'Synthex es control puro, mente fría y cálculo letal.Cada paso es un algoritmo, cada ataque una fórmula.Ganan con estrategia, dominan con disciplina total.No sienten presión. La ejecutan.',
            'summary': 'Macrojuego, control de mapa, ejecución táctica.Reinan en MOBAs, RTS y shooters estratégicos.No improvisan. Solo optimizan.',
            'image': 'images/Synthex.png',
            'link': '#',
            'button_text': 'Saber Más'
        },
        {
            'title': 'Furia cinética, sin tregua ni reversa',
            'description': 'Ravex es impacto inmediato y reacción salvaje. Viven al límite, rompen líneas y revientan mapas.Aceleran hasta borrar al enemigo del radar. El caos no los consume. Ellos lo crean.',
            'summary': 'Agresión explosiva, entrada frontal, ritmo constante. Dominan shooters, battle royale y juegos frenéticos. Cazan rápido. Caen tarde. Huyen nunca.',
            'image': 'images/ravex.png',
            'link': '#',
            'button_text': 'Saber Más'
        }
    ]

    return cards

