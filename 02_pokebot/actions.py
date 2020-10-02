from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.events import AllSlotsReset, Restarted
from rasa_sdk.executor import CollectingDispatcher

from typing import Any, Text, Dict, List, Union, Optional

import requests

POKEAPI_URL = "https://pokeapi.co/api/v2/"

POKEMON_TIPOS = {
    "normal": "normal", 
    "fighting": "lucha", 
    "flying": "volador", 
    "poison": "veneno", 
    "ground": "tierra", 
    "rock": "roca", 
    "bug": "bicho", 
    "ghost": "fantasma", 
    "steel": "acero", 
    "fire": "fuego", 
    "water": "agua", 
    "grass": "planta", 
    "electric": "eléctrico", 
    "psychic": "psíquico", 
    "ice": "hielo", 
    "dragon": "dragón", 
    "dark": "siniestro", 
    "fairy": "hada"
}

class ActionBuscarPokemon(Action):
    def name(self):
        return "action_buscar_pokemon"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        nombre_pokemon = tracker.get_slot("nombre_pokemon")
        numero_pokemon = tracker.get_slot("numero_pokemon")

        if nombre_pokemon and not numero_pokemon:
            req = requests.get(POKEAPI_URL + "pokemon/" + nombre_pokemon.lower())
        elif numero_pokemon and not nombre_pokemon:
            req = requests.get(POKEAPI_URL + "pokemon/" + numero_pokemon)
        
        if req.status_code == 404:
            dispatcher.utter_message(template="utter_pokemon_no_encontrado")
            return [AllSlotsReset()]

        info = req.json()
        info_numero_pokemon = str(info.get("id"))
        info_nombre_pokemon = info.get("name").title()
        info_tipos_pokemon = ", ".join([POKEMON_TIPOS.get(t.get("type").get("name")) for t in info.get("types")])
        info_imagen_pokemon = info.get("sprites").get("front_default")
        if info_imagen_pokemon:
            dispatcher.utter_message(
                template="utter_info_pokemon",
                numero=info_numero_pokemon,
                nombre=info_nombre_pokemon,
                tipos=info_tipos_pokemon,
                imagen=info_imagen_pokemon
            )
        else:
            dispatcher.utter_message(
                template="utter_info_pokemon_sin_imagen",
                numero=info_numero_pokemon,
                nombre=info_nombre_pokemon,
                tipos=info_tipos_pokemon
            )
        return [AllSlotsReset()]
